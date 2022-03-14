import flask

__site = flask.Flask(__name__)


@__site.route('/')
def home() -> str:
    return flask.render_template('home.html')


@__site.route('/about')
def about() -> str:
    return flask.render_template('about.html')


if __name__ == '__main__':
    __site.run()
