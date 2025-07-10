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
        month     = request.args.get('month')  # 前端传入两位月，如 '06'

        if car_type not in TABLE_MAP:
            return jsonify({'error': '非法 car_type'}), 400

        prefix = TABLE_MAP[car_type]
        # 如果不是 all 类型，需要 month 参数
        if car_type != 'all':
            if not month or not month.isdigit() or not (1 <= int(month) <= 12):
                return jsonify({'error': '缺少或非法 month 参数'}), 400
            # 补全两位
            month_str = month.zfill(2)
            table = f"{prefix}{month_str}"
        else:
            table = 'car_sales'

        # 获取 DB 配置并连接
        db_conf = current_app.config.get('DB_CONFIG')
        if not db_conf:
            return jsonify({'error':'DB_CONFIG 未配置'}), 500
        db_conf = db_conf.copy()
        db_conf['cursorclass'] = pymysql.cursors.DictCursor

        conn = pymysql.connect(**db_conf)
        try:
            with conn.cursor() as cur:
                sql = (
                    f"SELECT image_url, car_name, ranking, rating, price_range, sales "
                    f"FROM `{table}` ORDER BY ranking"
                )
                cur.execute(sql)
                results = cur.fetchall()
        finally:
            conn.close()

        return jsonify(results), 200

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 500


@api.route('/car-sales-trend')
def get_car_sales_trend():
    """
    接收 ?type=sedan|suv|mpv|all&start=MM&end=MM
    返回 { months: [...], totals: [...] }
    """
    try:
        car_type = request.args.get('type', 'all')
        start    = request.args.get('start')  # e.g. "02"
        end      = request.args.get('end')    # e.g. "06"

        # 校验
        if car_type not in TABLE_MAP:
            return jsonify({'error': '非法 type 参数'}), 400
        if car_type != 'all':
            if not (start and end and start.isdigit() and end.isdigit()):
                return jsonify({'error': '缺失或非法 start/end 参数'}), 400
            si, ei = int(start), int(end)
            # 简单不跨年区间校验，可根据需要改成循环区间
            if si < 1 or si > 12 or ei < 1 or ei > 12:
                return jsonify({'error': 'start/end 必须在 01-12 之间'}), 400
        else:
            # all 类型忽略月份
            si = ei = None

        # DB 连接配置
        db_conf = current_app.config.get('DB_CONFIG')
        if not db_conf:
            return jsonify({'error': 'DB_CONFIG 未配置'}), 500
        dbc = db_conf.copy()
        dbc['cursorclass'] = pymysql.cursors.DictCursor

        # 确定要查询的前缀列表
        if car_type == 'all':
            prefixes = ['jiaoche_', 'suv_', 'mpv_']
        else:
            prefixes = [TABLE_MAP[car_type]]

        # 构建月份列表（MM字符串）
        months_int = []
        if car_type == 'all':
            # all 类型，用最近 5 个月：往前推 5 月（含 end 月为当月）
            now = pymysql.datetime.datetime.now()
            curm = now.month
            for i in range(5):
                m = curm - (4 - i)
                if m <= 0: m += 12
                months_int.append(m)
        else:
            # 普通类型：从 start 到 end 顺序
            m = si
            while True:
                months_int.append(m)
                if m == ei:
                    break
                m += 1
                if m > 12:
                    m = 1
        # 转为两位
        months = [f"{m:02d}" for m in months_int]

        # 查询每个月总销量
        conn = pymysql.connect(**dbc)
        totals = []
        try:
            with conn.cursor() as cur:
                for mon in months:
                    if car_type == 'all':
                        # 三张表合并
                        parts = []
                        for p in prefixes:
                            parts.append(f"SELECT SUM(sales) AS tot FROM `{p}{mon}`")
                        union = " UNION ALL ".join(parts)
                        sql = f"SELECT SUM(tot) AS month_total FROM ({union}) AS sub"
                    else:
                        tbl = f"{prefixes[0]}{mon}"
                        sql = f"SELECT SUM(sales) AS month_total FROM `{tbl}`"
                    cur.execute(sql)
                    row = cur.fetchone()
                    totals.append(row['month_total'] or 0)
        finally:
            conn.close()

        return jsonify({'months': months, 'totals': totals}), 200

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 500

