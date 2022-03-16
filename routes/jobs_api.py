import flask

blueprint = flask.Blueprint(
    'jobs',
    __name__,
    template_folder='templates',
    url_prefix="/api/jobs"
)


@blueprint.route('/')
def get_news():
    return "Обработчик в job_api"


@blueprint.route('/<int:news_id>')
def get_news_by_id(news_id):
    return f"Обработчик в job_api {news_id}"
