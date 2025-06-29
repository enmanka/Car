# -*- coding:utf-8 -*-
import json

from flask import Blueprint, jsonify, request
from flask_cors import CORS

import hashlib
import secrets

from house.config import db
from house.dbmodule.bank_trend import BankTrend
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

@data.route('/getCarSales')
def get_car_sales():
    month = request.args.get('month')  # 拿到顾客要求的月份
    
    # 从数据库（CarSales表）筛选数据
    query = CarSales.query.filter_by(month=month)\
                         .order_by(CarSales.sales.desc())\
                         .limit(5)
    for item in query:
        print(item.car_name, item.sales)

    
    # 把数据打包成JSON（外卖盒）
    return jsonify([
        {"car_name": item.car_name, "sales": item.sales} 
        for item in query
    ])

# 注册接口
@data.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # 检查用户名是否存在
    if User.query.filter_by(usr_name=data['usr_name']).first():
        return jsonify({"error": "用户名已存在"}), 400
    
    # 创建新用户
    new_user = User(
        usr_name=data['usr_name'],
        pwd=generate_password_hash(data['pwd'])  # 存储salt:iterations:hash
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
        "user": {"username": user.usr_name}
    })

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
