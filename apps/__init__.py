# -*- coding:utf-8 -*-
from flask import Flask

from apps.chkperf.view.perf import perf
from apps.config import Config
from apps.ext import init_ext


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    init_ext(app)
    register_blueprint(app)
    return app


def register_blueprint(app):
    app.register_blueprint(perf)
