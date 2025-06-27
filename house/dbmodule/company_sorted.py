from house.config import db

class CompanySorted(db.Model):
    __tablename__ = "company_sorted"
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50))
    score = db.Column(db.DECIMAL)
