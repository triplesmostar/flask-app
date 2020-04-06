import jinja2
from flask import Flask
from flask_alembic import Alembic

from .controllers import bpp
from .general import build_error_response
from .db import db
from .models import *  # This one is important for Alembic auto generated migrations to work
from .settings import environments
from werkzeug.exceptions import default_exceptions
from .general import CustomLogException, FlaskProjectLogException

#Dodati import router od svakoga controllera
from .controllers.test_category_controller import router
from .controllers.test_film_controller import router


def create_app(config_environment):
    app = Flask('FlaskProject')

    config_object = environments[config_environment]()
    config_object.init_app(app)

    db.init_app(app)

    # Initialize flask-alembic
    alembic = Alembic()
    alembic.init_app(app)

    # Mount blueprints
    app.register_blueprint(bpp)

    # Log starting of application instance
    app.logger.info(
        "Starting Flask '{0}' in '{1}' mode".format(
            app.name, config_environment
        )
    )

    jinja2.ChoiceLoader([
        app.jinja_loader,
        jinja2.FileSystemLoader('/FlaskProject/templates'),
    ])

    _initialize_global_exception_handler(app)

    return app


def _initialize_global_exception_handler(app):
    for code, ex in default_exceptions.items():
        app.errorhandler(code)(build_error_response)

    @app.errorhandler(404)
    def _unhandled_any_error(e):
        """
        Global, any-unhandled-exception handler.
        Returns API error JSON response.
        """
        return build_error_response(CustomLogException(e))

    @app.errorhandler(500)
    def _unhandled_any_error(e):
        """
        Global, any-unhandled-exception handler.
        Returns API error JSON response.
        """
        return build_error_response(CustomLogException(e))

    @app.errorhandler(Exception)
    def _unhandled_any_error(e):
        """
        Global, any-unhandled-exception handler.
        Returns API error JSON response.
        """
        return build_error_response(CustomLogException(e))

    @app.errorhandler(FlaskProjectLogException)
    def _unhandled_any_error(e):
        """
        Global, any-unhandled-exception handler.
        Returns API error JSON response.
        """
        return build_error_response(CustomLogException(e))
