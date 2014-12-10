# -*- coding:utf-8 -*-
__author__ = 'Administrator'


class ApplicationException(Exception):
	def __init__(self, message):
		self.message = message

	def __str__(self):
		return self.message
