# -*- coding:utf-8 -*-
import json

from flask import Blueprint, jsonify, request
from flask_cors import CORS
from sqlalchemy import func
import csv
import io
from datetime import datetime
from flask import Response 
from urllib.parse import quote

import hashlib
import secrets

from house.config import db
from house.dbmodule.bank_trend import BankTrend
from house.dbmodule.car_follow import CarFollow
from house.dbmodule.city_count import CityCount
from house.dbmodule.company_amont import CompanyAmont
from house.dbmodule.company_sorted import CompanySorted
from house.dbmodule.economic_active import EconomicActive
from house.dbmodule.every_regions_ershoufang_count import EveryRegionsErshoufangCount
from house.dbmodule.every_regions_zufang_count import EveryRegionsZufangCount
from house.dbmodule.fang_wu_zheng_shou import FangWuZhengShou
from house.dbmodule.gong_zu_fang import GongZuFang
#from house.dbmodule.serven_area import ServenArea
from house.dbmodule.car_sales import CarSales
from house.dbmodule.user import User
from house.dbmodule.yu_shou_trend import YuShouTrend
from house.dbmodule.zufang_shoufang_price_compare import ZufangShoufangPriceCompare
from house.dbmodule.car_month import CarMonth
from house.dbmodule.export_record import ExportRecord

from sqlalchemy import text
from urllib.parse import quote 

"""
本视图专门用于处理ajax数据
"""
data = Blueprint('data', __name__)
CORS(data)


# 生成密码哈希（使用PBKDF2算法）
def generate_password_hash(password):
    salt = secrets.token_hex(16)  # 生成随机盐值
    iterations = 100000  # 迭代次数增强安全性
    hashed = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        iterations
    )
    return f"{salt}:{iterations}:{hashed.hex()}"

# 验证密码
def check_password_hash(hashed_password, input_password):
    salt, iterations, stored_hash = hashed_password.split(':')
    new_hash = hashlib.pbkdf2_hmac(
        'sha256',
        input_password.encode('utf-8'),
        salt.encode('utf-8'),
        int(iterations)
    )
    return stored_hash == new_hash.hex()

@data.route('/exportCarSalesCSV')
def export_car_sales_csv():
    car_type = request.args.get('type', 'jiaoche')
    month = request.args.get('month', '01')
    user_name = request.args.get('user_name')  # 从前端获取用户名
    if not user_name:
        return Response("缺少用户名参数", status=400)

    table_name = f"{car_type}_{month}"  # 例如 jiaoche_01

    try:
        sql = text(f"SELECT ranking, car_name, sales, rating, price_range FROM {table_name} ORDER BY ranking LIMIT 50")
        result = db.session.execute(sql).fetchall()
    except Exception as e:
        return Response(f"查询失败: {str(e)}", status=500)

    # 构造 CSV 数据
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['排名', '车型', '销量', '口碑评分', '价格区间'])  # 表头
    for row in result:
        writer.writerow(row)

    now = datetime.now()
    now_str = now.strftime('%Y%m%d_%H%M%S')
    filename = f"{car_type}_{month}_销量榜_{now_str}.csv"

    # 插入导出记录
    try:
        export_record = ExportRecord(
            user_name=user_name,
            export_time=now,
            csv_filename=filename
        )
        db.session.add(export_record)
        db.session.commit()
    except Exception as e:
        # 如果插入记录失败，打印错误仍返回文件
        print(f"插入导出记录失败: {e}")

    response = Response(output.getvalue().encode('utf-8-sig'), mimetype='text/csv')
    response.headers['Content-Disposition'] = f"attachment; filename*=UTF-8''{quote(filename)}"

    return response

@data.route('/getExportRecords')
def get_export_records():
    user_name = request.args.get('user_name')
    if not user_name:
        return jsonify({'error': '缺少用户名参数'}), 400

    try:
        records = ExportRecord.query.filter_by(user_name=user_name).order_by(ExportRecord.export_time.desc()).all()
        # 转成可json化格式
        records_list = [{
            'id': r.id,
            'user_name': r.user_name,
            'export_time': r.export_time.strftime('%Y-%m-%d %H:%M:%S'),
            'csv_filename': r.csv_filename
        } for r in records]
        return jsonify(records_list)
    except Exception as e:
        return jsonify({'error': f'查询失败: {str(e)}'}), 500

import traceback

@data.route('/getCarSalesByMonthAndType', methods=['GET'])
def get_car_sales_by_month_type():
    car_type = request.args.get('type')
    month = request.args.get('month')

    if not car_type or not month:
        return jsonify({"error": "缺少参数"}), 400

    try:
        CarMonth.set_table(car_type, month)  # 这里应该有打印
        # 使用 session.execute 查询表
        sql = CarMonth.__table__.select()
        result = db.session.execute(sql).all()

        items = []
        for row in result:
            items.append({
                "id": row.id,
                "car_type": row.car_type,
                "ranking": row.ranking,
                "car_name": row.car_name,
                "sales": row.sales,
                "rating": row.rating,
                "price_range": row.price_range,
                "image_url": row.image_url
            })
        return jsonify(items)

    except Exception as e:
        tb = traceback.format_exc()
        print(tb)  # 服务器终端打印完整异常栈，方便查错
        return jsonify({"error": str(e), "trace": tb}), 500


@data.route('/getCarFollow')
def get_car_follow():

    # 找出北京关注度前十的汽车名
    beijing_top_ten = (
        db.session.query(CarFollow.car_name)
        .filter(CarFollow.city_range == '北京')
        .order_by(CarFollow.follow.desc())
        .limit(18)
        .all()
    )
    beijing_top_ten_car_names = [item.car_name for item in beijing_top_ten]

    if not beijing_top_ten_car_names:
        return jsonify([])

    # 查询其他城市这些汽车的关注度
    result = (
        db.session.query(CarFollow.city_range, CarFollow.car_name, CarFollow.follow)
        .filter(
            CarFollow.car_name.in_(beijing_top_ten_car_names),
            CarFollow.city_range != '北京'
        )
        .all()
    )

    # 格式化数据
    items = []
    for row in result:
        items.append({
            "car_name": row.car_name,
            "city_range": row.city_range,
            "follow": row.follow
        })

    # 把数据打包成 JSON 并返回
    return jsonify(items)

@data.route('/update_avatar', methods=['POST'])
def update_avatar():
    data = request.get_json()
    username = data.get('usr_name')
    avatar_index = data.get('avatar_index')

    if not username or not avatar_index:
        return jsonify({'error': '参数不完整'}), 400

    user = User.query.filter_by(usr_name=username).first()
    if not user:
        return jsonify({'error': '用户不存在'}), 404

    user.avatar_index = avatar_index
    db.session.commit()

    return jsonify({'message': '头像更新成功'}), 200

@data.route('/getCarSales')
def get_acar_sales():
    month = request.args.get('month')  # 拿到顾客要求的月份
    
    # 从数据库（CarSales表）筛选数据
    query = CarSales.query.filter_by(month=month)\
                         .order_by(CarSales.sales.desc())\
                         .limit(5)
    # for item in query:
    #     print(item.car_name, item.sales)

    
    # 把数据打包成JSON（外卖盒）
    return jsonify([
        {"car_name": item.car_name, "sales": item.sales} 
        for item in query
    ])

@data.route('/getAllCarSales')
def get_all_car_sales():
    result = (
        db.session.query(
            CarSales.car_name,
            func.sum(CarSales.sales).label("total_sales")
        )
        .group_by(CarSales.car_name)
        .order_by(func.sum(CarSales.sales).desc())
        .limit(30)
        .all()
    )
    
    # 转换Decimal为int并格式化数据
    wordcloud_data = [
        {
            "name": name,
            "value": int(total_sales)  # 将Decimal转换为int
        } 
        for name, total_sales in result
    ]
    return jsonify(wordcloud_data)

@data.route('/getCarSales_All')
def getCarSales_All():
    # 从数据库（CarSales表）获取所有数据
    all_car_sales = CarSales.query.all()
    count = request.args.get('count', type=int, default=15)

    # 用于存储按 car_name 汇总的销售数据
    car_sales_summary = {}

    # 遍历所有数据，按 car_name 对 sales 进行求和
    for item in all_car_sales:
        car_name = item.car_name
        sales = item.sales
        if car_name in car_sales_summary:
            car_sales_summary[car_name] += sales
        else:
            car_sales_summary[car_name] = sales
        print(car_name,car_sales_summary[car_name])

    # 将汇总结果转换为列表格式，并按总销量降序排序
    result = [{"car_name": car_name, "total_sales": total_sales} for car_name, total_sales in car_sales_summary.items()]
    result.sort(key=lambda x: x["total_sales"], reverse=True)

    # 仅取前十个数据
    # result = result[:15]
    result = result[:count]

    # 把数据打包成 JSON 并返回
    return jsonify(result)

@data.route('/getCarSalesByMonth')
def get_car_sales_by_month():
    # 获取请求参数中的月份
    month = request.args.get('month')
    
    if not month or not month.isdigit() or int(month) not in range(1, 13):
        return jsonify({"error": "Invalid month parameter"}), 400
    
    # 查询指定月份的数据
    result = (
        db.session.query(
            CarSales.car_name,
            func.sum(CarSales.sales).label("total_sales")
        )
        .filter(func.extract('month', CarSales.sales) == int(month))
        .group_by(CarSales.car_name)
        .order_by(func.sum(CarSales.sales).desc())
        .limit(30)
        .all()
    )
    
    # 转换Decimal为int并格式化数据
    wordcloud_data = [
        {
            "name": name,
            "value": int(total_sales)  # 将Decimal转换为int
        } 
        for name, total_sales in result
    ]
    
    return jsonify(wordcloud_data)

# 注册接口
@data.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # 检查用户名是否存在
    if User.query.filter_by(usr_name=data['usr_name']).first():
        return jsonify({"error": "用户名已存在"}), 400
    
    # 获取头像索引，若未提供则默认值为 1
    avatar_index = data.get('avatar_index', 1)

    # 创建新用户
    new_user = User(
        usr_name=data['usr_name'],
        pwd=generate_password_hash(data['pwd']),  # 注意这里添加逗号
        avatar_index=avatar_index  # 修正参数赋值格式
    )
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "注册成功"}), 201

# 登录接口
@data.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(usr_name=data['usr_name']).first()
    
    if not user or not check_password_hash(user.pwd, data['pwd']):
        return jsonify({"error": "用户名或密码错误"}), 401
    
    # 生成简单token（实际生产环境需要更安全的方案）
    token = secrets.token_urlsafe(32)
    
    return jsonify({
        "message": "登录成功",
        "token": token,
        "username": user.usr_name,
        "avatar_index": user.avatar_index
    })

@data.route('/change_password', methods=['POST'])
def change_password():
    data = request.get_json()

    usr_name = data.get('usr_name')
    old_pwd = data.get('old_pwd')
    new_pwd = data.get('new_pwd')

    if not usr_name or not old_pwd or not new_pwd:
        return jsonify({"error": "参数不完整"}), 400

    user = User.query.filter_by(usr_name=usr_name).first()
    if not user:
        return jsonify({"error": "用户不存在"}), 404

    if not check_password_hash(user.pwd, old_pwd):
        return jsonify({"error": "旧密码错误"}), 401

    # 更新新密码
    user.pwd = generate_password_hash(new_pwd)
    db.session.commit()

    return jsonify({"message": "密码修改成功"}), 200

@data.route('/getMap', methods=['GET'])
def get_map():
    data = db.session.query(CityCount).all()
    view_data = {}
    view_data["series"] = []

    def build_view_data(item):
        dic = {}
        dic["value"] = item.count
        dic["name"] = item.city
        view_data["series"].append([dic])

    [build_view_data(item) for item in data]

    return json.dumps(view_data, ensure_ascii=False)


@data.route('/getZufangShoufangPriceCompare', methods=['GET'])
def get_zufang_shoufang_price_compare():
    data = db.session.query(ZufangShoufangPriceCompare).all()
    view_data = {}
    view_data["xAxis"] = ["华北", "华东", "东北", "华中", "华南", "西南", "西北"]
    view_data["series1"] = []
    view_data["series2"] = []
    all_area = ["华北", "华东", "东北", "华中", "华南", "西南", "西北"]

    def build_view_data(item):
        tmp_dic = {}
        tmp_dic["price"] = item.price
        tmp_dic["city"] = item.city
        if item.data_type == "zufang":
            view_data["series1"].append(item.price)
        else:
            view_data["series2"].append(item.price)

    [build_view_data(item) for i in all_area for item in data if item.city == i]

    return json.dumps(view_data, ensure_ascii=False)


@data.route('/getEveryRegionsZufangCount', methods=['GET'])
def get_every_regions_zufang_count():
    data = db.session.query(EveryRegionsZufangCount).all()
    view_data = {}
    view_data["xAxis"] = ["华北", "华东", "东北", "华中", "华南", "西南", "西北"]
    view_data["series1"] = []
    all_area = ["华北", "华东", "东北", "华中", "华南", "西南", "西北"]

    def build_view_data(item):
        tmp_dic = {}
        tmp_dic["value"] = item.count
        tmp_dic["name"] = item.city
        view_data["series1"].append(tmp_dic)

    [build_view_data(item) for i in all_area for item in data if item.city == i]

    return json.dumps(view_data, ensure_ascii=False)


@data.route('/getEveryRegionsErshoufangCount', methods=['GET'])
def get_every_regions_ershoufang_count():
    data = db.session.query(EveryRegionsErshoufangCount).all()
    view_data = {}
    view_data["xAxis"] = ["华北", "华东", "东北", "华中", "华南", "西南", "西北"]
    view_data["series1"] = []
    all_area = ["华北", "华东", "东北", "华中", "华南", "西南", "西北"]

    def build_view_data(item):
        tmp_dic = {}
        tmp_dic["value"] = item.count
        tmp_dic["name"] = item.city
        view_data["series1"].append(tmp_dic)

    [build_view_data(item) for i in all_area for item in data if item.city == i]

    return json.dumps(view_data, ensure_ascii=False)


@data.route('/getEconomicActive', methods=['GET'])
def get_economic_active():
    data = db.session.query(EconomicActive).all()
    view_data = {}
    view_data["series1"] = []

    def build_view_data(item):
        view_data["series1"].append(item.city)

    [build_view_data(item) for item in data]

    return json.dumps(view_data, ensure_ascii=False)


@data.route('/getFangWuZhengShou', methods=['GET'])
def get_fang_wu_zheng_shou():
    data = db.session.query(FangWuZhengShou).all()
    view_data = {}
    view_data["series1"] = []

    def build_view_data(item):
        tmp_dic = {}
        tmp_dic["name"] = item.area
        tmp_dic["value"] = item.counter
        view_data["series1"].append(tmp_dic)

    [build_view_data(item) for item in data]

    return json.dumps(view_data, ensure_ascii=False)


@data.route('/getYuShouTrend', methods=['GET'])
def get_yu_shou_trend():
    data = db.session.query(YuShouTrend).order_by(YuShouTrend.year.asc()).all()
    view_data = {}
    view_data["year"] = []
    view_data["area"] = []

    def build_view_data(item):
        view_data["area"].append(item.area)
        view_data["year"].append(item.year)

    [build_view_data(item) for item in data]

    return json.dumps(view_data, ensure_ascii=False)


@data.route('/getGongZuFang', methods=['GET'])
def get_gong_zu_fang():
    data = db.session.query(GongZuFang).all()
    view_data = {}
    view_data["xAxis"] = []
    view_data["series1"] = []
    view_data["series2"] = []

    def build_view_data(item):
        view_data["xAxis"].append(item.location)
        view_data["series1"].append(item.counter)
        view_data["series2"].append(item.area)

    [build_view_data(item) for item in data]

    return json.dumps(view_data, ensure_ascii=False)


@data.route('/getCompanySorted', methods=['GET'])
def get_company_sorted():
    order = request.args.get("order")
    if order == "1":
        data = db.session.query(CompanySorted).order_by(CompanySorted.score.desc()).all()[0:5]
    else:
        data = db.session.query(CompanySorted).order_by(CompanySorted.score.asc()).all()[0:5]

    view_data = {}
    view_data["series"] = []

    def build_view_data(item):
        view_data["series"].append({"value": item.score, "name": item.city})

    [build_view_data(item) for item in data]

    return json.dumps(view_data, ensure_ascii=False)


@data.route('/getBankTrend', methods=['GET'])
def get_bank_trend():
    data = db.session.query(BankTrend).order_by(BankTrend.year.asc()).all()
    view_data = {}
    view_data["year"] = []
    view_data["amount"] = []

    def build_view_data(item):
        view_data["year"].append(item.year)
        view_data["amount"].append(item.amount)

    [build_view_data(item) for item in data]

    return json.dumps(view_data, ensure_ascii=False)


@data.route('/getCompanyAmont', methods=['GET'])
def get_company_amont():
    data = db.session.query(CompanyAmont).all()
    view_data = {}
    view_data["series"] = []

    def build_view_data(item):
        dic = {}
        dic["value"] = item.amount
        dic["name"] = item.company_name
        view_data["series"].append(dic)

    [build_view_data(item) for item in data]

    return json.dumps(view_data, ensure_ascii=False)

