"""Flask configuration variables."""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SESSION_TYPE = os.environ.get('SESSION_TYPE') or 'filesystem'
    MAX_CONTENT_LENGTH = os.environ.get('MAX_CONTENT_LENGTH') or 16 * 1000 * 1000
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')