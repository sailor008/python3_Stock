"""
FileName: Stock-block-list.py
查询股票板块列表
"""

""" 接口示范
host = 'https://ali-stock.showapi.com'
path = '/stock-block-list'
method = 'GET'
appcode = '你自己的AppCode'
querys = ''
bodys = {}
url = host + path
"""


# import system module
import json

import g_var
import Logger
import DataManager
import NetworkMgr


m_csvFileName = 'stock-block-list.csv'
m_apiUrl = 'https://ali-stock.showapi.com'
m_apiKeyword = '/stock-block-list'

def onSuccessRequest(bodyData):
	Logger.log("is onSuccessRequest:: ---- %s"%str(bodyData))
	if bodyData != None and bodyData.get("list") != None:
		listData = bodyData.get("list")
		Logger.log("item.count = %s"%len(listData))
		if(len(listData) <= 0):
			return
		# for classifyList in listData:
		DataManager.saveJsonDataToFile(m_csvFileName, listData)



#拼接url
# url = m_apiUrl + m_apiKeyword
# NetworkMgr.requestURLWithGet(url, onSuccessRequest)




fileData = DataManager.readOriginalDataFile("stock_block_list.txt")
if fileData != None:
	jsonData = json.loads(fileData)
	print(type(jsonData))
	if jsonData != None and jsonData.get("list") != None:
		listData = jsonData.get("list")
		for classifyInfo in listData:
			print("分类名称：%s"%classifyInfo.get("name"))
else:
	print("------------file is not esixt()")
