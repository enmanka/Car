from house.config import db
class CarSales(db.Model):
    __tablename__ = "car_sales"
    id = db.Column(db.Integer, primary_key=True)      # 唯一ID（类似Excel行号）
    car_name = db.Column(db.String(50))               # 车型名称（文本，最大50字）
    sales = db.Column(db.Integer)                     # 销量（整数）
    month = db.Column(db.Integer)                     # 月份（1-12月）