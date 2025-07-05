from flask import Blueprint, request, jsonify
from sqlalchemy import text
from house.config import db
from house.models import Comment,CommentLike


comment_bp = Blueprint('comment', __name__, url_prefix='/api/comment')

@comment_bp.route('/', methods=['GET'])
def list_comments():
    car_name = request.args.get('car_name')
    if not car_name:
        return jsonify({'error': '缺少 car_name 参数'}), 400

    comments = (Comment.query
                      .filter_by(car_name=car_name)
                      .order_by(Comment.created_at.desc())
                      .all())
    data = [{
        'id': c.id,
        'usr_name': c.usr_name,
        'content': c.content,
        'like_count': c.like_count,
        'created_at': c.created_at.strftime('%Y-%m-%d %H:%M:%S')
    } for c in comments]
    return jsonify(data), 200


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
