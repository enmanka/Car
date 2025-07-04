from house.config import db
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)      # 唯一ID（类似Excel行号）
    usr_name = db.Column(db.String(50))              
    pwd = db.Column(db.String(50))   
    avatar_index=db.Column(db.Integer)                  