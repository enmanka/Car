from house.config import db


class CityCount(db.Model):
    __tablename__ = "city_count"
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50))
    count = db.Column(db.INTEGER)
