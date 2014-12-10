# -*- coding:utf-8 -*-
__author__ = 'Administrator'
from ffcs.config.form.handler import FormHandler

urls = [
	(r'/form/(.*)', FormHandler),
]