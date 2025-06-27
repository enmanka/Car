from house.config import db


class EveryRegionsZufangCount(db.Model):
    __tablename__ = "every_regions_zufang_count"
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50))
    count = db.Column(db.INTEGER)
