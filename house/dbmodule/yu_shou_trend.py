from house.config import db

class YuShouTrend(db.Model):
    __tablename__ = "yu_shou_trend"
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(50))
    year = db.Column(db.INTEGER)
