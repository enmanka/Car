from house.config import db


class GongZuFang(db.Model):
    __tablename__ = "gong_zu_fang"
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(50))
    counter = db.Column(db.INTEGER)
    area = db.Column(db.DECIMAL)
