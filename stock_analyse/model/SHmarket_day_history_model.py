"""
FileName: SHmarket_day_history_model
大盘历史查询
"""

""" 接口示范
host = 'https://ali-stock.showapi.com'
path = '/indexDayHis'
method = 'GET'
appcode = '你自己的AppCode'
querys = 'code=000001&month=201703'
bodys = {}
url = host + path + '?' + querys
"""


# import system module
import json

import g_var
import Logger
import DataManager
import NetworkMgr


m_csvFileName = 'shMarket-day-history.csv'
m_apiUrl = 'https://ali-stock.showapi.com'
m_apiKeyword = '/indexDayHis'

def onSuccessRequest(bodyData):
	Logger.log("is onSuccessRequest:: ---- %s"%str(bodyData))
	if bodyData != None and bodyData.get("list") != None:
		listData = bodyData.get("list")
		Logger.log("item.count = %s"%len(listData))
		if(len(listData) <= 0):
			return
		# for classifyList in listData:
		DataManager.saveJsonDataToFile(m_csvFileName, listData)

## 拼接url, sendRequest
querys = 'code=000001&month=201712'
url = m_apiUrl + m_apiKeyword + '?' + querys
NetworkMgr.requestURLWithGet(url, onSuccessRequest)


### 使用队列进行网络请求 【注意：未完成，待学习！！！】
def sendRequestQueue(monthArray):
	Logger.log("is sendRequestQueue")




