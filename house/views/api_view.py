# 文件：house/views/api_view.py
from flask import Blueprint, request, jsonify, current_app
import pymysql, traceback

api = Blueprint('api', __name__, url_prefix='/api')

# 只映射三种类型的前缀；month 参数保证 01~05
TABLE_MAP = {
    'sedan': 'jiaoche_',  # 轿车
    'suv':   'suv_',      # SUV
    'mpv':   'mpv_',      # MPV
    'all':   None         # 主表 car_sales
}

@api.route('/car-sales')
def get_car_sales():
    try:
        car_type = request.args.get('type', 'all')
        month    = request.args.get('month', '01')
        # 参数校验
        if car_type not in TABLE_MAP or month not in ['01','02','03','04','05']:
            return jsonify({'error': '参数非法'}), 400

        # 动态拼接表名
        if car_type == 'all':
            table = 'car_sales'
        else:
            table = f"{TABLE_MAP[car_type]}{month}"

        sql = f"""
            SELECT image_url, car_name, ranking, rating, price_range, sales
              FROM `{table}`
             ORDER BY ranking
        """

        # 从 app.config 获取 DB_CONFIG 并设置 cursorclass
        db_conf = current_app.config.get('DB_CONFIG')
        if not db_conf:
            return jsonify({'error':'DB_CONFIG 未配置，请检查 config.py'}),500
        db_conf = db_conf.copy()
        db_conf['cursorclass'] = pymysql.cursors.DictCursor

        conn = pymysql.connect(**db_conf)
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                results = cur.fetchall()
        finally:
            conn.close()

        return jsonify(results)

    except Exception as e:
        # 打印堆栈到终端
        traceback.print_exc()
        # 返回错误详情给前端
        return jsonify({
            'error': str(e),
            'trace': traceback.format_exc()
        }), 500

@api.route('/car-sales-trend')
def get_car_sales_trend():
    try:
        car_type = request.args.get('type', 'all')
        start    = request.args.get('start', '01')
        end      = request.args.get('end',   '05')
        # 校验参数
        if car_type not in TABLE_MAP or start not in ['01','02','03','04','05'] or end not in ['01','02','03','04','05']:
            return jsonify({'error':'参数非法'}), 400
        if int(start) > int(end):
            return jsonify({'months': [], 'totals': []})

        # 拿配置
        db_conf = current_app.config.get('DB_CONFIG')
        if not db_conf:
            return jsonify({'error':'DB_CONFIG 未配置'}), 500
        db_conf = db_conf.copy()
        db_conf['cursorclass'] = pymysql.cursors.DictCursor

        # 构造月份列表
        months = [f"{m:02d}" for m in range(int(start), int(end)+1)]
        totals = []

        # 建立连接
        conn = pymysql.connect(**db_conf)
        try:
            with conn.cursor() as cur:
                # 逐月累加
                for mon in months:
                    if car_type == 'all':
                        # all 聚合三大类
                        sql_parts = []
                        for prefix in ['jiaoche_','suv_','mpv_']:
                            sql_parts.append(f"SELECT SUM(sales) AS total FROM `{prefix}{mon}`")
                        sql = " UNION ALL ".join(sql_parts)
                        # UNION ALL 后需要再累加
                        sql = f"SELECT SUM(total) AS month_total FROM ({sql}) AS sub"
                    else:
                        prefix = TABLE_MAP[car_type]
                        sql = (
                            f"SELECT SUM(sales) AS month_total "
                            f"FROM `{prefix}{mon}`"
                        )
                    cur.execute(sql)
                    row = cur.fetchone()
                    totals.append(row['month_total'] or 0)
        finally:
            conn.close()

        return jsonify({'months': months, 'totals': totals})

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error':str(e), 'trace': traceback.format_exc()}), 500

