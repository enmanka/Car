from house.config import db


class ZufangShoufangPriceCompare(db.Model):
    __tablename__ = "zufang_shoufang_price_compare"
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50))
    price = db.Column(db.DECIMAL)
    data_type = db.Column(db.String(50))
