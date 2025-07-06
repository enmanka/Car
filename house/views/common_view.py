# 文件：house/views/common_view.py

from flask import Blueprint, request, jsonify
from sqlalchemy import text
from house.config import db

# ✅ 这里定义 blueprint，必须放在所有 route 装饰器之前
common_bp = Blueprint('common', __name__, url_prefix='/api')
@common_bp.route('/carType')
def get_car_type():
    model = request.args.get('model')
    if not model:
        return jsonify({"error": "missing model"}), 400

    prefixes = ['suv', 'mpv', 'jiaoche']
    months   = ['01', '02', '03', '04', '05']

    for prefix in prefixes:
        for m in months:
            tbl = f"{prefix}_{m}"
            try:
                exists = db.session.execute(text("SHOW TABLES LIKE :t"), {"t": tbl}).fetchone()
                if not exists:
                    continue
                result = db.session.execute(
                    text(f"SELECT 1 FROM {tbl} WHERE car_name = :c LIMIT 1"),
                    {"c": model}
                ).fetchone()
                if result:
                    return jsonify({"type": prefix})
            except Exception as e:
                print(f"Error checking table {tbl}: {e}")  # 调试用
                continue

    return jsonify({"type": None})
