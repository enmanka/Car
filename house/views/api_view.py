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
    动态检测最后月份后缀（表名中的数字部分），然后往前取 5 个月，
    统计各月销售总量。
    """
    try:
        car_type = request.args.get('type', 'all')
        if car_type not in TABLE_MAP:
            return jsonify({'error': '非法 car_type'}), 400

        # 从 app.config 获取 DB_CONFIG 并设置 cursorclass
        db_conf = current_app.config.get('DB_CONFIG')
        if not db_conf:
            return jsonify({'error': 'DB_CONFIG 未配置'}), 500
        db_conf = db_conf.copy()
        db_conf['cursorclass'] = pymysql.cursors.DictCursor

        # 确定表名前缀
        if car_type == 'all':
            prefixes = ['jiaoche_', 'suv_', 'mpv_']
        else:
            prefixes = [TABLE_MAP[car_type]]

        # 1) 查询 information_schema 找到所有后缀
        conn = pymysql.connect(**db_conf)
        try:
            with conn.cursor() as cur:
                suffixes = set()
                for prefix in prefixes:
                    cur.execute(
                        "SELECT TABLE_NAME FROM information_schema.TABLES "
                        "WHERE TABLE_SCHEMA=%s AND TABLE_NAME LIKE %s",
                        (db_conf.get('db') or db_conf.get('database'), prefix + '%')
                    )
                    for row in cur.fetchall():
                        # 提取表名后面的数字部分
                        name = row['TABLE_NAME']
                        num_part = name.replace(prefix, '')
                        if num_part.isdigit():
                            suffixes.add(int(num_part))
                if not suffixes:
                    return jsonify({'months': [], 'totals': []})

                # 2) 取最大后缀作为最后一个月份
                max_month = max(suffixes)

                # 3) 构造向前 5 个月的列表（不低于 1）
                months_int = [m for m in range(max_month, max_month - 5, -1) if m >= 1]
                # 按时间从远到近，再翻转为近到远
                months_int.sort()
                months = [f"{m:02d}" for m in months_int]

                # 4) 对每个前缀、每个月份累加销售
                totals = []
                for mon in months:
                    if car_type == 'all':
                        # all 需要把三张表合并再求和
                        sql_parts = []
                        for prefix in prefixes:
                            sql_parts.append(
                                f"SELECT SUM(sales) AS total FROM `{prefix}{mon}`"
                            )
                        union_sql = " UNION ALL ".join(sql_parts)
                        sql = f"SELECT SUM(total) AS month_total FROM ({union_sql}) AS sub"
                    else:
                        sql = (
                            f"SELECT SUM(sales) AS month_total "
                            f"FROM `{prefixes[0]}{mon}`"
                        )
                    cur.execute(sql)
                    row = cur.fetchone()
                    totals.append(row['month_total'] or 0)

        finally:
            conn.close()

        return jsonify({'months': months, 'totals': totals}), 200

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 500

