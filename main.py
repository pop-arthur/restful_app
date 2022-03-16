from flask import Flask, jsonify
from data.db_session import global_init
from routes import jobs_blueprint, news_blueprint
from flask import make_response


app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



def main():
    global_init("db/blogs.db")
    app.register_blueprint(jobs_blueprint)
    app.register_blueprint(news_blueprint)
    app.run()


if __name__ == '__main__':
    main()
