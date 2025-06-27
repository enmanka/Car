from house.config import db


class ServenArea(db.Model):
    __tablename__ = "serven_area"
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50))
    price = db.Column(db.DECIMAL)
