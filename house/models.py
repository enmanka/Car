# 文件：house/models.py

from datetime import datetime
from house.config import db

class Comment(db.Model):
    __tablename__ = 'comment'

    id         = db.Column(db.BigInteger, primary_key=True, autoincrement=True, comment='评论自增主键')
    usr_name   = db.Column('usr_name', db.String(50), db.ForeignKey('user.usr_name'), nullable=False, comment='关联 user.usr_name')
    car_name   = db.Column('car_name', db.String(100), nullable=False, index=True, comment='车型名称')
    content    = db.Column('content', db.Text, nullable=False, comment='评论内容')
    like_count = db.Column('like_count', db.Integer, default=0, nullable=False, comment='点赞数')
    created_at = db.Column('created_at', db.DateTime, default=datetime.utcnow, nullable=False, comment='发表时间')

    def __repr__(self):
        return f"<Comment id={self.id} usr_name={self.usr_name} car_name={self.car_name}>"

class CommentLike(db.Model):
    __tablename__ = 'comment_like'

    usr_name   = db.Column(db.String(50), db.ForeignKey('user.usr_name'), primary_key=True)
    comment_id = db.Column(db.BigInteger, db.ForeignKey('comment.id'), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

