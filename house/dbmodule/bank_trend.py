from house.config import db


class BankTrend(db.Model):
    __tablename__ = "bank_trend"
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.INTEGER)
    amount = db.Column(db.DECIMAL)
