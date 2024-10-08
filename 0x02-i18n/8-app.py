#!/usr/bin/env python3
"""Basic Flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from crypt import methods
from email import header
import pytz


class Config:
    """ Config for app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """returns a user dictionary or None if the ID cannot be found
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """summary
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    Gates locale from request object
    """
    locale = request.args.get("locale")
    if locale:
        return locale
    user = request.args.get("login_as")
    if user:
        lang = users.get(int(user)).get('locale')
        if lang in app.config['LANGUAGES']:
            return lang
    headers = request.headers.get("locale")
    if headers:
        return headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    get_timezone.
    """
    try:
        timezone = request.args.get("timezone")
        if timezone:
            return pytz.timezone(timezone)
        user = request.args.get("login_as")
        if user:
            timezone = users.get(int(user)).get('timezone')
            if timezone:
                return pytz.timezone(timezone)
        timezone = request.headers.get("timezone")
        if timezone:
            return pytz.timezone(timezone)
    except pytz.UnknownTimeZoneError:
        return app.config.get('BABEL_DEFAULT_TIMEZONE')
    return app.config.get('BABEL_DEFAULT_TIMEZONE')


@app.route('/')
def index():
    """ basic route """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
