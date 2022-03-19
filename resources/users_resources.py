from flask import jsonify
from flask_restful import abort, reqparse, Resource

from data import db_session
from data.db_session import create_session
from data.users import User


def abort_if_user_not_found(user_id):
    session = create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UserResource(Resource):
    def get(self, news_id):
        abort_if_user_not_found(news_id)
        session = create_session()
        user = session.query(User).get(news_id)
        return jsonify({'user': user.to_dict()})

    def delete(self, news_id):
        abort_if_user_not_found(news_id)
        session = create_session()
        user = session.query(User).get(news_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict() for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        news = User(
            id=args['id'],
            name=args['name'],
            about=args['about'],
            email=args['email'],
            hashed_password=args['hashed_password'],
            created_date=args['created_date']
        )
        session.add(news)
        session.commit()
        return jsonify({'success': 'OK'})


parser = reqparse.RequestParser()
parser.add_argument('id', required=True)
parser.add_argument('name', required=True)
parser.add_argument('about', required=True)
parser.add_argument('email', required=True)
parser.add_argument('hashed_password', required=True)
parser.add_argument('created_date', required=True)
