import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    APP_DIR = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqliteext:///%s' % os.path.join(APP_DIR, 'blog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = os.environ['SECRET_KEY']

    # Blog configuration values.
    # You may consider using a one-way hash to generate the password, and then
    # use the hash again in the login view to perform the comparison. This is just
    # for simplicity.
    ADMIN_PASSWORD = 'secret'

    # The playhouse.flask_utils.FlaskDB object accepts database URL configuration.
    DATABASE = 'sqliteext:///%s' % os.path.join(APP_DIR, 'blog.db')
    DEBUG = False

    # The secret key is used internally by Flask to encrypt session data stored
    # in cookies. Make this unique for your app.
    SECRET_KEY = 'shhh, secret!'

    # This is used by micawber, which will attempt to generate rich media
    # embedded objects with maxwidth=800.
    SITE_WIDTH = 800

