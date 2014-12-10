# -*- coding:utf-8 -*-
__author__ = 'Administrator'

from xml.etree.ElementTree import fromstring
from ffcs.util.ApplicationException import ApplicationException


class XmlHelper(object):
	XML_HEAD = "<?xml version=\"1.0\" encoding=\"utf-8\"?>"
	SUCCESS_XML = "<root><error_code>0</error_code></root>"
	ERROR_XML = "<root><error_code>1</error_code></root>"

	@classmethod
	def Encode(cls, str):
		v_str = "" if str is None else str
		for a in str:
			if a == "&":
				v_str += "&amp;"
			elif a == "<":
				v_str += "&lt;"
			elif a == ">":
				v_str += "&gt;"
			elif a == "\"":
				v_str += "&quot;"
			else:
				v_str += a
		return v_str

	@classmethod
	def cursorToXml(cls, cursor):
		xmlReturn = list()
		xmlReturn.append("<root>")
		xmlReturn.append("<rows>")
		colNames = [colName[0] for colName in cursor.description]
		for row in cursor.fetchall():
			xmlReturn.append("<row>")
			for i in xrange(0, len(colNames)):
				tagName = colNames[i].lower()
				xmlReturn.append("<")
				xmlReturn.append(tagName)
				xmlReturn.append(">")
				xmlReturn.append(str(row[i]).decode('utf-8'))
				xmlReturn.append("</")
				xmlReturn.append(tagName)
				xmlReturn.append(">")
			xmlReturn.append("</row>")
		xmlReturn.append("</rows>")
		xmlReturn.append("</root>")
		return "".join(xmlReturn)

	@classmethod
	def getSingleParam(cls, xmlString, nodeName):
		root = fromstring(xmlString)
		try:
			ele = root.find(nodeName)
			return ele.text
		except:
			raise ApplicationException('解析xml单一参数出错')

	@classmethod
	def getMultiElement2ToModelSql(cls, xmlString):
		root = fromstring(xmlString)
		models = dict()
		for ele in root.getchildren(): # Forms
			for ele2 in ele.getchildren(): # forms
				obj = dict()
				for ele3 in ele2.getchildren():
					obj[ele3.tag] = ele3.text
				models.setdefault(ele2.tag, list()).append(obj)
		return XmlHelper.getModel2InsertSql(models)

	@classmethod
	def getModel2InsertSql(cls, modelDict):
		sqls = list()
		for k, v in modelDict.items():
			for item in v:
				sql = list()
				values = list()
				sql.append("insert into ")
				sql.append(k)
				sql.append("(")
				for field, value in item.items():
					sql.append(str(field))
					sql.append(",")
					values.append("'")
					values.append(str(value))
					values.append("'")
					values.append(",")
				sql = sql[:-1]
				values = values[:-1]
				sql.append(") values(")
				sql.extend(values)
				sql.append(")")
				sql.append(";")
				sql.append("\n")
				sqls.append("".join(sql))
		return "".join(sqls)






