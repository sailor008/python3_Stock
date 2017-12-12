# FileNam: Stock_block_model.py

# import system module
import json

import g_var


m_csvFilePath = g_var.get('DataPath')+'name-to-stockinfo'
m_apiUrl = 'http://stock.market.alicloudapi.com'
m_apiKeyword = '/name-to-stockinfo'


# respData = NetworkMgr.requestDataByGet(m_apiUrl + m_apiKeyword, 'code=002739&name=%E4%B8%87%E8%BE%BE')

jsonString = "{\"showapi_res_code\":0,\"showapi_res_error\":\"\",\"showapi_res_body\":{\"ret_code\":0,\"list\":[{\"min_price\":\"11.510\",\"market\":\"sh\",\"trade_num\":\"17541504\",\"trade_money\":\"215834624\",\"close_price\":\"12.480\",\"open_price\":\"11.700\",\"code\":\"600004\",\"max_price\":\"12.700\",\"date\":\"2015-09-02\"},{\"min_price\":\"11.920\",\"market\":\"sh\",\"trade_num\":\"8111935\",\"trade_money\":\"99310240\",\"close_price\":\"12.110\",\"open_price\":\"12.680\",\"code\":\"600004\",\"max_price\":\"12.680\",\"date\":\"2015-09-01\"}]}}"

m_list = {}
bodyData = parseResponeData(jsonString)
if bodyData != None and bodyData.get("list") != None:
	m_list = bodyData.get("list")
	print("keys = %s"%len(m_list))
	if(len(m_list) > 0):
		fileObj = open(m_csvFilePath, 'a+')
		writer = csv.DictWriter(fileObj, m_list[0].keys())
		writer.writeheader()

def saveListDataToCSV(filePath, listData):
