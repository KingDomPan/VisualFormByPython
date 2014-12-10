# -*- coding:utf-8 -*-
__author__ = 'Administrator'

from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
	def get(self):
		return self.render('index.html', name='panqd')