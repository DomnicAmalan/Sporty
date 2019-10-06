
from flask import Flask, request, render_template
from app.routes.client.controllers import client
from app.routes.admin.controllers import admin
from app.config import configure_app
from app.utils import get_instance_folder_path
from app.data.models import db
import logging
from app.cache import cache, cache_config

app = Flask(__name__, instance_path=get_instance_folder_path(),
            instance_relative_config=True,
            template_folder='templates')

cache.init_app(app, cache_config)

configure_app(app)

app.register_blueprint(client, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')


@app.errorhandler(404)
def page_not_found(error):
	app.logger.error('Page not found: %s', (request.path))
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return render_template('500.htm'), 500

@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception: %s', (e))
    return render_template('500.htm'), 500