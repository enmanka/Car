from house.config import db

class EconomicActive(db.Model):
    __tablename__ = "economic_active"
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50))
    count = db.Column(db.INTEGER)
    price = db.Column(db.DECIMAL)
