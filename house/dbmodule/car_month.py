from sqlalchemy import Table, MetaData
from house.config import db

class CarMonth(db.Model):
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    car_type = db.Column(db.String(50))
    ranking = db.Column(db.Integer)
    car_name = db.Column(db.String(100))
    sales = db.Column(db.Integer)
    rating = db.Column(db.Float(3, 2))
    price_range = db.Column(db.String(50))
    image_url = db.Column(db.String(255))

    @classmethod
    def set_table(cls, category, month):
        table_name = f"{category}_{month}"
        metadata = MetaData()
        cls.__table__ = Table(table_name, metadata, autoload_with=db.engine)
        print(f"绑定表: {table_name}")
