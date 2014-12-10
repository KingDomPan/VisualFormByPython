# -*- coding:utf-8 -*-
__author__ = 'Administrator'

import os
import sys

from tornado.web import asynchronous
from tornado.web import RequestHandler
from tornado.web import HTTPError

from ffcs.util import dbconfig
from ffcs.util.XmlHelper import XmlHelper
from ffcs.util.ApplicationException import ApplicationException


reload(sys)
sys.setdefaultencoding('utf-8')

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


class FormHomeHandler(RequestHandler):
	@asynchronous
	def get(self):
		return self.render('form/index.html')

	@asynchronous
	def post(self):
		return self.get()


class FormHandler(RequestHandler):
	def callback(self, methodName, xmlString=None):
		method = getattr(FormDao, methodName)
		if callable(method):
			return method(xmlString)

	@asynchronous
	def get(self, methodName):
		print methodName, '----------------'
		print self.request.method, '-------------method---------------' # GET POST
		print self.request.uri, '-------------uri---------------' # /form/get_flow_mod?id=1
		print self.request.path, '-------------path---------------' # /form/get_flow_mod
		print self.request.query, '-------------query---------------' # 暂时没
		print self.request.body, '-------------body---------------' # xml字符串
		self.set_header("Content-Type", 'text/xml')
		try:
			self.write(self.callback(methodName, self.request.body))
			self.finish()
		except ApplicationException, ex:
			raise HTTPError(500, ex.message)

	@asynchronous
	def post(self, methodName):
		return self.get(methodName)


class FormDao(object):
	GET_FLOW_MOD = "SELECT COUNT(*) FROM FLOW_MODEL WHERE FLOW_MOD=:flow_mod"
	GET_TABLE_FIELDS = "SELECT COLUMN_NAME VALUE,COLUMN_NAME text from user_tab_columns where table_name=:table_name"
	GET_FORM_ID = "SELECT FORM_ID_SEQ.NEXTVAL form_id FROM DUAL"
	GET_TACHE_MODEL = "SELECT TCH_MOD VALUE,TCH_MOD||'('||TCH_NAME||')' text \
										FROM TACHE_MODEL WHERE FLOW_MOD=:flow_mod order by 1"

	@classmethod
	def get_flow_mod(cls, xmlString):
		conn = dbconfig.getConn()
		cursor = conn.cursor()
		flow_mod = XmlHelper.getSingleParam(xmlString, 'flow_mod')
		try:
			cursor.execute(cls.GET_FLOW_MOD, {'flow_mod': flow_mod})
			result = cursor.fetchone()
			if result is not None:
				return FormDao.get_tache_model(flow_mod)
		except Exception,e:
			print e
			raise ApplicationException('获取flow_mod出错')
		finally:
			dbconfig.close(conn, cursor)

	@classmethod
	def get_tache_model(cls, flow_mod):
		conn = dbconfig.getConn()
		cursor = conn.cursor()
		try:
			cursor.execute(cls.GET_TACHE_MODEL, {'flow_mod': flow_mod})
			return XmlHelper.cursorToXml(cursor)
		except Exception,e:
			print e
			raise ApplicationException('获取tache_mod出错')
		finally:
			dbconfig.close(conn, cursor)

	@classmethod
	def get_table_fields(cls, xmlString):
		conn = dbconfig.getConn()
		cursor = conn.cursor()
		table_name = XmlHelper.getSingleParam(xmlString, 'table_name')
		try:
			cursor.execute(cls.GET_TABLE_FIELDS, {'table_name': table_name})
			return XmlHelper.cursorToXml(cursor)
		except:
			raise ApplicationException('获取table_fields出错')
		finally:
			dbconfig.close(conn, cursor)

	@classmethod
	def get_form_id(cls, xmlString):
		conn = dbconfig.getConn()
		cursor = conn.cursor()
		try:
			cursor.execute(cls.GET_FORM_ID)
			return XmlHelper.cursorToXml(cursor)
		except:
			raise ApplicationException('获取form_id出错')
		finally:
			dbconfig.close(conn, cursor)

	@classmethod
	def push_into_table(cls, xmlString):
		isqls = XmlHelper.getMultiElement2ToModelSql(xmlString)
		f = open("d:\\test.sql", "w")
		f.write(isqls)
		f.close()
		return XmlHelper.SUCCESS_XML

	@classmethod# JUST FOR TEST
	def test(cls, xmlString):
		table_names = XmlHelper.getSingleParam(xmlString, "table_names")
		table_name_array = table_names.split(",")
		for tb in table_name_array:
			sql = "SELECT '{name:'||''''||lower(COLUMN_NAME)||'''}' AS col \
					FROM user_tab_columns where table_name=upper(:table_name) order by 1"
			conn = dbconfig.getConn()
			cursor = conn.cursor()
			try:
				cursor.execute(sql, {'table_name': tb})
				head = list()
				km = list()
				head.append("var ")
				head.append(str(tb).lower().capitalize())
				head.append("=new Ext.data.Record.create([")
				for row in cursor.fetchall():
					km.append(str(row[0]))
					km.append(",")
				km = km[:-1]
				head.extend(km)
				head.append("]);")
				print "".join(head)
			except:
				raise ApplicationException('获取form_id出错')
			finally:
				dbconfig.close(conn, cursor)
