"""Flask configuration variables."""
from os import environ, path
import util
from dotenv import load_dotenv
import logging

#  for complete flask_sqlachemy config parameters and session handling,
#  read: file flask_sqlalchemy/__init__.py AND flask/config.py
'''
app.config.setdefault('SQLALCHEMY_DATABASE_URI', 'sqlite:///:memory:')
app.config.setdefault('SQLALCHEMY_BINDS', None)
app.config.setdefault('SQLALCHEMY_NATIVE_UNICODE', None)
app.config.setdefault('SQLALCHEMY_ECHO', False)
app.config.setdefault('SQLALCHEMY_RECORD_QUERIES', None)
app.config.setdefault('SQLALCHEMY_POOL_SIZE', None)
app.config.setdefault('SQLALCHEMY_POOL_TIMEOUT', None)
app.config.setdefault('SQLALCHEMY_POOL_RECYCLE', None)
app.config.setdefault('SQLALCHEMY_MAX_OVERFLOW', None)
app.config.setdefault('SQLALCHEMY_COMMIT_ON_TEARDOWN', False)
'''

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, "default.env"))
app_logger = logging.getLogger('api_logic_server_app')


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
    DEBUG = environ.get("DEBUG")

    # Database
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #                          'sqlite:///' + os.path.join(basedir, 'app.db') + '?check_same_thread=False'
    SQLALCHEMY_DATABASE_URI = "sqlite:////workspaces/ApiLogicProject/database/db.sqlite"

    # begin patch to set db_url for sqlite (only)  XXXXX
    #   since sqlite db is copied to created project, we can set db_url here
    from pathlib import Path
    running_at = Path(__file__)
    project_abs_dir = running_at.parent.absolute()
    # project_abs_dir = project_abs_dir.parent.absolute()
    # print(f'project_abs_dir: {project_abs_dir}')
    db_loc = str(project_abs_dir) + "/database/db.sqlite"
    db_url = "sqlite:///" + db_loc
    app_logger.debug(f'config.py - db_url: {db_url}')
    SQLALCHEMY_DATABASE_URI = db_url
    # end patch to set db_url for sqlite (only)

    # override SQLALCHEMY_DATABASE_URI here as required

    app_logger.debug(f'config.py - SQLALCHEMY_DATABASE_URI: {SQLALCHEMY_DATABASE_URI}')

    # SQLALCHEMY_ECHO = environ.get("SQLALCHEMY_ECHO")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = False

