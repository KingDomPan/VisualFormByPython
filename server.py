# -*- coding:utf-8 -*-
__author__ = 'Administrator'
import sys

import tornado.ioloop
from application import application


PORT = '8080'
if __name__ == '__main__':
	if len(sys.argv) > 1:
		PORT = sys.argv[1]
	application.listen(PORT)
	print 'Development server is running at http://localhost:%s/' % PORT
	print 'Quit the server with Control-C'
	ioloop = tornado.ioloop.IOLoop.instance()
	ioloop.start()