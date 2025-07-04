from house.config import db
from datetime import datetime

class ExportRecord(db.Model):
    __tablename__ = "export_records"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(50), nullable=False)
    export_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    csv_filename = db.Column(db.String(255), nullable=False)