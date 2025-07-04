from house.config import db
class CarFollow(db.Model):
    __tablename__ = "car_follow_city"
    id = db.Column(db.Integer, primary_key=True)      # 唯一ID（类似Excel行号）
    car_name = db.Column(db.String(50))
    score=db.Column(db.String(50))
    price=db.Column(db.String(50))
    follow=db.Column(db.Integer)
    city_range=db.Column(db.String(50))
    # 车型名称（文本，最大50字）
