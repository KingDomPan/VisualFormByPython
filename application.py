# -*- coding:utf-8 -*-
__author__ = 'Administrator'
import os
import tornado.web
from tornado.web import StaticFileHandler
from ffcs.config.form.handler import FormHomeHandler
from ffcs.config.handler import BaseHandler
from ffcs.config.form.handler import FormHandler

SETTINGS = dict(
	template_path=os.path.join(os.path.dirname(__file__), 'templates'),
	static_path=os.path.join(os.path.dirname(__file__), 'static'),
	debug=True,
)

DATA_PATH = SETTINGS['static_path'] + '/data/'

urls = [
	(r'/(favicon\.ico)', StaticFileHandler, dict(path=SETTINGS['static_path'])),
	(r'/data/(?P<path>.*)$', StaticFileHandler, dict(path=DATA_PATH)),
	(r'/form', FormHomeHandler),
	(r'/form/(?P<methodName>.*)$', FormHandler),
	(r'/', BaseHandler)
]

application = tornado.web.Application(
	handlers=urls,
	**SETTINGS
)