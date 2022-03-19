from flask import Flask, jsonify, make_response
from flask_restful import Api

from data.db_session import global_init
from resources.users_resources import UserResource, UsersListResource
from routes import jobs_blueprint, news_blueprint
from resources import NewsListResource, NewsResource


app = Flask(__name__)
api = Api(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def main():
    global_init("db/blogs.db")
    app.register_blueprint(jobs_blueprint)
    app.register_blueprint(news_blueprint)
    api.add_resource(UserResource, "/api/v2/users/<int:news_id>")
    api.add_resource(UsersListResource, "/api/v2/users")
    app.run()


if __name__ == '__main__':
    main()
