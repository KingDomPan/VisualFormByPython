# -*- coding:utf-8 -*-
__author__ = 'Administrator'
import cx_Oracle
from DBUtils.PooledDB import PooledDB

db_config = dict(
	username='XXXXXX_kf',
	password='XXXXXX',
	encoding='utf-8',
	dsn=cx_Oracle.makedsn('192.168.1.1', 21001, 'itmtest)')
)


class DbManager(object):
	def __init__(self):
		#connKwargs = {'user': db_config['username'], 'password': db_config['password'],
		#			  'dsn': db_config['dsn'], 'encoding': db_config['encoding']}
		#self._pool = PooledDB(cx_Oracle, mincached=0, maxcached=10, maxshared=10, maxusage=10000, **connKwargs)
		self._pool = PooledDB(cx_Oracle, user="XXXXXX_kf", password="XXXXXX", dsn="192.168.1.1:21001/itmtest",
							  mincached=2, maxcached=2, maxshared=2, maxconnections=2)

	def getConn(self):
		return self._pool.connection()

	@classmethod
	def close(cls, conn, cursor):
		if cursor is not None:
			cursor.close()
		if conn is not None:
			conn.close()


_dbManager = DbManager()


def getConn():
	return _dbManager.getConn()


def close(conn, cursor):
	DbManager.close(conn, cursor)