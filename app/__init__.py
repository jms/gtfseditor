__version__ = '1.2.10'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS
from config import config
from flask.ext.login import LoginManager
from flask_mail import Mail
from flask_admin import Admin
from flask.ext.bootstrap import Bootstrap
from flask.ext.compress import Compress
from celery import Celery

from .admin.views import MyAdminIndexView


db = SQLAlchemy()
mail = Mail()
cors = CORS()
compress = Compress()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
admin = Admin(name='gtfseditor', template_mode='bootstrap3', index_view=MyAdminIndexView())


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    compress.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    app.config['CORS_HEADERS'] = 'X-Requested-With, Content-Type'
    cors.init_app(app)
    admin.init_app(app)

    # if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
    #     from flask.ext.sslify import SSLify
    #     sslify = SSLify(app)

    from .admin import register_admin_views
    register_admin_views(admin)


    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')


    from .editor import editor as editor_blueprint

    if app.config['DEBUG']:
        editor_blueprint.static_folder = 'static/app'
    else:
        editor_blueprint.static_folder = 'static/dist'

    app.register_blueprint(editor_blueprint, url_prefix='/editor')

    register_blueprints(app)

    from .ng_editor import ng_editor as ng_editor_bp

    if app.config['DEBUG']:
        ng_editor_bp.static_folder = 'static/app'
    else:
        ng_editor_bp.static_folder = 'static/dist'

    app.register_blueprint(ng_editor_bp, url_prefix='/ng-editor')


    from .reports import reports as reports_blueprint
    app.register_blueprint(reports_blueprint, url_prefix='/reports')


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')


    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)


    return app


def create_celery_app(app=None):
    app = app or create_app('staging')
    celery = Celery(__name__)
    celery.conf.update(app.config)

    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask

    from .tasks import register_tasks

    register_tasks(celery)

    return celery

def register_blueprints(app):
    from app.agencies import agencies_bp
    app.register_blueprint(agencies_bp, url_prefix='/editor/agencies')

    from app.routes import routes_bp
    app.register_blueprint(routes_bp, url_prefix='/editor/routes')

    from app.trips import trips_bp
    app.register_blueprint(trips_bp, url_prefix='/editor/routes')

def register_extensions(app):
    pass
