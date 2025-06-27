from house.config import db


class CompanyAmont(db.Model):
    __tablename__ = "company_amont"
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(50))
    amount = db.Column(db.DECIMAL)
