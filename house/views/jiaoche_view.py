# house/views/mpv_view.py

from flask import Blueprint, request, jsonify
from sqlalchemy import text
from house.config import db
from datetime import datetime

jiaoche_bp = Blueprint('jiaoche', __name__, url_prefix='/api/jiaoche')

def gen_months(start: str, end: str):
    """生成从 start 到 end（包含两端）的所有月份列表，格式 YYYY-MM"""
    m1 = datetime.strptime(start, "%Y-%m")
    m2 = datetime.strptime(end,   "%Y-%m")
    months = []
    while m1 <= m2:
        months.append(m1.strftime("%Y-%m"))
        if m1.month == 12:
            m1 = m1.replace(year=m1.year+1, month=1)
        else:
            m1 = m1.replace(month=m1.month+1)
    return months

@jiaoche_bp.route('/models')
def jiaoche_models():
    """
    返回指定区间（startMonth~endMonth）内所有 mpv_xx 表中出现过的 car_name 列表
    JSON 响应：{ models: [...] }
    """
    start = request.args.get('startMonth', '2025-01')
    end   = request.args.get('endMonth',   '2025-05')
    months = gen_months(start, end)

    models = set()
    for m in months:
        tbl = f"jiaoche_{m[-2:]}"
        if not db.session.execute(text("SHOW TABLES LIKE :t"), {"t": tbl}).fetchone():
            continue
        rows = db.session.execute(text(f"SELECT DISTINCT car_name FROM {tbl}")).fetchall()
        models |= {r[0] for r in rows}

    return jsonify(models=sorted(models))


@jiaoche_bp.route('/monthly')
def jiaoche_monthly():
    """
    两种模式：
      1) 不带 model，返回：
         { months: [...],
           series: [ {model:'GL8', data:[…]}, … ] }
      2) 带 model，返回：
         { months: [...],
           rows: [
             { month, model, sales, ranking, rating, price_range, image_url },
             …
           ],
           imageUrl: "…"
         }
    """
    start = request.args.get('startMonth', '2025-01')
    end   = request.args.get('endMonth',   '2025-05')
    model = request.args.get('model', None)
    months = gen_months(start, end)

    # 若单车查询，预先抓一次 image_url
    image_url = None
    if model:
        for m in months:
            tbl = f"jiaoche_{m[-2:]}"
            if not db.session.execute(text("SHOW TABLES LIKE :t"), {"t": tbl}).fetchone():
                continue
            row = db.session.execute(
                text(f"SELECT image_url FROM {tbl} WHERE car_name = :c LIMIT 1"),
                {"c": model}
            ).fetchone()
            if row and row[0]:
                image_url = row[0]
                break

    # 组装车型列表
    if model:
        models = [model]
    else:
        models = set()
        for m in months:
            tbl = f"jiaoche_{m[-2:]}"
            if not db.session.execute(text("SHOW TABLES LIKE :t"), {"t": tbl}).fetchone():
                continue
            rows = db.session.execute(text(f"SELECT DISTINCT car_name FROM {tbl}")).fetchall()
            models |= {r[0] for r in rows}
        models = sorted(models)

    # 按月拉取所有字段
    data   = {mod: [] for mod in models}
    detail = {mod: [] for mod in models}

    for m in months:
        tbl = f"jiaoche_{m[-2:]}"
        if not db.session.execute(text("SHOW TABLES LIKE :t"), {"t": tbl}).fetchone():
            for mod in models:
                data[mod].append(0)
                detail[mod].append({})
            continue

        rows = db.session.execute(text(f"""
            SELECT ranking, car_name, sales, rating, price_range, image_url
            FROM {tbl}
        """)).fetchall()

        sales_map =     {r.car_name: r.sales       for r in rows}
        detail_map = {
            r.car_name: {
                "ranking":     r.ranking,
                "rating":      float(r.rating) if r.rating is not None else None,
                "price_range": r.price_range or "",
                "image_url":   r.image_url or None
            }
            for r in rows
        }

        for mod in models:
            data[mod].append(sales_map.get(mod, 0))
            detail[mod].append(detail_map.get(mod, {}))

    # 返回
    if model:
        # 单车：按月输出完整行
        rows_out = []
        for idx, mon in enumerate(months):
            info = detail[model][idx]
            rows_out.append({
                "month":       mon,
                "model":       model,
                "sales":       data[model][idx],
                "ranking":     info.get("ranking"),
                "rating":      info.get("rating"),
                "price_range": info.get("price_range"),
                "image_url":   info.get("image_url")
            })
        return jsonify(months=months, rows=rows_out, imageUrl=image_url)

    # 全量
    series = [{"model": m, "data": data[m]} for m in models]
    return jsonify(months=months, series=series)
