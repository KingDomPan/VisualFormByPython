__author__ = 'Administrator'
from xml.etree import ElementTree

query = "id=2&aa=2"

c = dict(map(lambda item: (str(item.split('=')[0]), str(item.split('=')[1])), query.split("&")))

print c

xml = r"<root><employee id = '1'><name>linux</name><age>30</age></employee><employee id = '2'><name>windows</name><age>20</age></employee></root>"
root = ElementTree.fromstring(xml)
for ele in root.getchildren():
	print ele.tag

xml2 = r"<Root><Forms><forms><form_id>212</form_id><form_name>aa</form_name></forms><forms><form_id>222</form_id><form_name>bb</form_name></forms></Forms></Root>"
def getMultiElement2ToModel(xmlString):
	root = ElementTree.fromstring(xmlString)
	models = dict()
	for ele in root.getchildren(): # Forms
		for ele2 in ele.getchildren(): # forms
			obj = dict()
			for ele3 in ele2.getchildren():
				obj[ele3.tag] = ele3.text
			models.setdefault(ele2.tag, list()).append(obj)
	return models


def getModel2InsertSql(modelDict):
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



print getModel2InsertSql(getMultiElement2ToModel(xml2))