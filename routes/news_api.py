from flask import Blueprint, jsonify, request

from data.db_session import create_session
from data.news import News

blueprint = Blueprint(
    'news_api',
    __name__,
    template_folder='templates',
    url_prefix="/api/news"
)


@blueprint.route('/')
def get_news():
    db_sess = create_session()
    news = db_sess.query(News).all()
    return jsonify(
        {
            'news':
                [item.to_dict(only=('title', 'content', 'user.name'))
                 for item in news]
        }
    )


@blueprint.route('/<int:news_id>', methods=['GET'])
def get_one_news(news_id):
    db_sess = create_session()
    news = db_sess.query(News).get(news_id)
    if not news:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'news': news.to_dict(only=(
                'title', 'content', 'user_id', 'is_private'))
        }
    )


@blueprint.route('/', methods=['POST'])
def create_news():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['title', 'content', 'user_id', 'is_private']):
        return jsonify({'error': 'Bad request'})
    db_sess = create_session()
    news = News(
        title=request.json['title'],
        content=request.json['content'],
        user_id=request.json['user_id'],
        is_private=request.json['is_private']
    )
    db_sess.add(news)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/<int:news_id>', methods=['DELETE'])
def delete_news(news_id):
    db_sess = create_session()
    news = db_sess.query(News).get(news_id)
    if news:
        db_sess.delete(news)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    else:
        return jsonify({'error': 'Not found'})


@blueprint.route('/<int:news_id>', methods=["PUT"])
def put_news(news_id):
    db_sess = create_session()
    news = db_sess.query(News).get(news_id)
    if news:
        if not request.json:
            return jsonify({'error': 'Empty request'})
        elif not any(key in request.json for key in
                     ['title', 'content', 'user_id', 'is_private']):
            return jsonify({'error': 'Bad request'})

        for key, new_value in request.json.items():
            setattr(news, key, new_value)

        db_sess.commit()
        return jsonify({'success': 'OK'})
    else:
        return jsonify({'error': 'Not found'})