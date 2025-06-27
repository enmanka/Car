from house.config import db

class FangWuZhengShou(db.Model):
    __tablename__ = "fang_wu_zheng_shou"
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(50))
    counter = db.Column(db.INTEGER)
