from flask import Blueprint, request, jsonify
from sqlalchemy import text
from house.config import db
from house.models import Comment,CommentLike


comment_bp = Blueprint('comment', __name__, url_prefix='/api/comment')

from datetime import datetime
import pytz  # 需要安装 pip install pytz

@comment_bp.route('/', methods=['GET'])
def list_comments():
    car_name = request.args.get('car_name')
    if not car_name:
        return jsonify({'error': '缺少 car_name 参数'}), 400

    comments = (Comment.query
                .filter_by(car_name=car_name)
                .order_by(Comment.created_at.desc())
                .all())
    
    # 转换为北京时间 (UTC+8)
    beijing_tz = pytz.timezone('Asia/Shanghai')
    
    data = []
    for comment in comments:
        # 确保时间是aware datetime对象
        utc_time = comment.created_at.replace(tzinfo=pytz.UTC)
        # 转换为北京时间
        beijing_time = utc_time.astimezone(beijing_tz)
        
        data.append({
            'id': comment.id,
            'usr_name': comment.usr_name,
            'content': comment.content,
            'like_count': comment.like_count,
            'created_at': beijing_time.strftime('%Y-%m-%d %H:%M')  # 格式化北京时间
        })
    
    return jsonify(data), 200

@comment_bp.route('/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    # 验证用户身份
    current_user = request.args.get('username')
    if not current_user:
        return jsonify({'error': '需要登录'}), 401
    
    # 获取评论
    comment = Comment.query.get_or_404(comment_id)
    
    # 验证评论所有者
    if comment.usr_name != current_user:
        return jsonify({'error': '只能删除自己的评论'}), 403
    
    try:
        # 先删除关联的点赞记录
        CommentLike.query.filter_by(comment_id=comment_id).delete()
        
        # 再删除评论
        db.session.delete(comment)
        db.session.commit()
        
        return jsonify({'message': '删除成功'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@comment_bp.route('/my_comments', methods=['GET'])
def get_my_comments():
    """获取当前用户的所有评论（按时间倒序）"""
    username = request.args.get('username')
    if not username:
        return jsonify({'error': '需要username参数'}), 400
    
    comments = Comment.query.filter_by(usr_name=username)\
                  .order_by(Comment.created_at.desc())\
                  .all()
    
    comments_data = [{
        'id': comment.id,
        'car_name': comment.car_name,
        'content': comment.content,
        'like_count': comment.like_count,
        'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')
    } for comment in comments]
    print(comments_data) 
    return jsonify(comments_data), 200

@comment_bp.route('/', methods=['POST'])
def post_comment():
    payload = request.get_json()
    car_name = payload.get('car_name')
    content  = payload.get('content')
    user     = payload.get('usr_name')

    if not all([car_name, content, user]):
        return jsonify({'error': '参数不全'}), 400

    c = Comment(usr_name=user, car_name=car_name, content=content)
    db.session.add(c)
    db.session.commit()
    return jsonify({'message': '评论发布成功','id':c.id}), 201



@comment_bp.route('/like', methods=['POST'])
def toggle_like():
    payload = request.get_json()
    cid  = payload.get('comment_id')
    user = payload.get('usr_name')

    if not all([cid, user]):
        return jsonify({'error': '参数不全'}), 400

    # 查询评论对象
    comment = Comment.query.get(cid)
    if not comment:
        return jsonify({'error': '评论不存在'}), 404

    # 查询是否已点赞
    existing = CommentLike.query.get((user, cid))
    if existing:
        # 已点赞，则取消：删除记录，评论表 like_count 减一
        db.session.delete(existing)
        comment.like_count = Comment.like_count - 1
        liked = False
    else:
        # 未点赞，则新增：插入记录，评论表 like_count 加一
        db.session.add(CommentLike(usr_name=user, comment_id=cid))
        comment.like_count = Comment.like_count + 1
        liked = True

    # 提交两张表的修改
    db.session.commit()

    return jsonify({
        'like_count': comment.like_count,
        'liked': liked
    }), 200
