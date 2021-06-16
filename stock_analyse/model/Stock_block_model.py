"""
FileName: Stock_block_model
查询股票的历史行情
"""


""" 接口示范
host = 'http://stock.market.alicloudapi.com'
path = '/sz-sh-stock-history'
method = 'GET'
appcode = '你自己的AppCode'
querys = 'begin=2015-09-01&code=600004&end=2015-09-02'
bodys = {}
url = host + path + '?' + querys
"""

# import system module
import json

import g_var
import Logger
import DataManager
import NetworkMgr


m_csvFilePath = g_var.get_value('DataPath')+'name-to-stockinfo'
m_apiUrl = 'http://stock.market.alicloudapi.com'
m_apiKeyword = '/name-to-stockinfo'

def onSuccessRequest(bodyData):
	print("is onSuccessRequest:: ---- %s"%str(bodyData))
	if bodyData != None and bodyData.get("list") != None:
		listData = bodyData.get("list")
		print("keys = %s"%len(listData))
		if(len(listData) <= 0):
			return
		DataManager.saveJsonDataToFile("name-to-stockinfo.csv", listData)

url = "http://stock.market.alicloudapi.com/sz-sh-stock-history?begin=2017-11-01&code=601006&end=2017-11-30"
NetworkMgr.requestGetFromAliAPI(url, onSuccessRequest)
