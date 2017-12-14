# FileNam: Stock_block_model.py

# import system module
import json

import Logger
import g_var


m_csvFilePath = g_var.get_value('DataPath')+'name-to-stockinfo'
m_apiUrl = 'http://stock.market.alicloudapi.com'
m_apiKeyword = '/name-to-stockinfo'


def saveListDataToCSV(filePath, listData):
	Logger.log("is saveListDataToCSV")



def onSuccessRequest(bodyData):
	print("is onSuccessRequest:: ---- %s"%str(bodyData))
	if bodyData != None and bodyData.get("list") != None:
		m_list = bodyData.get("list")
		print("keys = %s"%len(m_list))
	# if(len(m_list) > 0):
	# 	# 到此处的逻辑未处理--------------------------------------
	# 	fileObj = open(m_csvFilePath, 'a+')
	# 	writer = csv.DictWriter(fileObj, m_list[0].keys())
	# 	writer.writeheader()

# url = "http://stock.market.alicloudapi.com/name-to-stockinfo?code=601006"
# NetworkMgr.requestURLWithGet(url, onSuccessRequest)

bodyDic = {'ret_code': 0, 'list': [{'stockType': 'A', 'market': 'sh', 'name': '大秦铁路', 'state': 1, 'currcapital': '1486679.1491', 'profit_four': '132.5979', 'code': '601006', 'totalcapital': '1486679.1491', 'mgjzc': '6.552233', 'pinyin': 'dqtl', 'listing_date': '2006-08-01', 'ct': '2016-10-16 15:39:17.914'}]}
onSuccessRequest(bodyDic)