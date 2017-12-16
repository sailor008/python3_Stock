# import system module
import sys
import os
application_path = os.path.abspath('.')
# #把模块的路径加到当前的主程序中
sys.path.append(application_path+'/utils')
sys.path.append(application_path+'/showapi')
sys.path.append(application_path+'/model')


import constant
import g_var
g_var._init()#在主模块初始化全局变量的dic
# #定义当前的程序名称
g_var.set_value("ApplicationTag", "stock_analyse")
# #定义文件的根路径
g_var.set_value('ApplicationPath', application_path)
# #定义文件的根路径
g_var.set_value('DataPath', application_path+'/data')
# #定义跨模块全局变量
g_var.set_value('HOST','https://ali-stock.showapi.com-8')



import csv

#import custom code
import Logger
import FileHelper
import NetworkMgr
import DataManager

import api_func




# #>>>>-----初始化-----<<<<<
#注意：Logger的初始化必须比其他类早
Logger._init()
FileHelper._init()
DataManager._init()


# print("main_start>>> AppKey = %s, secret = %s"%(constant.AppKey, constant.AppSecret))

# api_func.request_stock_block_list()


# Logger.writeSingleLine("--->>>test_log565631", None)

import Stock_block_model




# # jsonString = "{\"showapi_res_code\": 0,\"showapi_res_error\": \"\",\"showapi_res_body\": {\"ret_code\": 0,list\": [{\"min_price\": \"11.510\",\"market\": \"sh\",\"trade_num\": \"17541504\",\"trade_money\": \"215834624\",\"close_price\": \"12.480\",\"open_price\": \"11.700\",\"code\": \"600004\",\"max_price\": \"12.700\",\"date\": \"2015-09-02\"},{\"min_price\": \"11.920\",\"market\": \"sh\",\"trade_num\": \"8111935\",\"trade_money\": \"99310240\",\"close_price\": \"12.110\",\"open_price\": \"12.680\",\"code\": \"600004\",\"max_price\": \"12.680\",\"date\": \"2015-09-01\"}]}}"
# jsonString = "{\"showapi_res_code\":0,\"showapi_res_error\":\"\",\"showapi_res_body\":{\"ret_code\":0,\"list\":[{\"min_price\":\"11.510\",\"market\":\"sh\",\"trade_num\":\"17541504\",\"trade_money\":\"215834624\",\"close_price\":\"12.480\",\"open_price\":\"11.700\",\"code\":\"600004\",\"max_price\":\"12.700\",\"date\":\"2015-09-02\"},{\"min_price\":\"11.920\",\"market\":\"sh\",\"trade_num\":\"8111935\",\"trade_money\":\"99310240\",\"close_price\":\"12.110\",\"open_price\":\"12.680\",\"code\":\"600004\",\"max_price\":\"12.680\",\"date\":\"2015-09-01\"}]}}"
# jsonAttrs = json.loads(jsonString)

# if jsonAttrs.get("showapi_res_code")!=None and jsonAttrs.get("showapi_res_code") == 0:
# 	print("is get data success!!!")
# else:
# 	print("Error:api respone result code!")
# print("====================\n")

# m_list = {}
# bodyData = jsonAttrs.get("showapi_res_body")
# if bodyData != None and bodyData.get("list") != None:
# 	m_list = bodyData.get("list")
# 	print("keys = %s"%len(m_list))
# 	print("obj.type = %s"%type(m_list[0]))
# 	if(len(m_list) > 0):
# 		fileObj = open(application_path+'/log_files/test.csv', '+')
# 		# writer = csv.DictWriter(fileObj, m_list[0].keys())
# 		# writer.writeheader()
# 		bVal = csv.Sniffer().has_header(fileObj.readline())
# 		fileObj.seek(0)
# 		if not bVal:
# 			print("writer header data to csv file!")
# 			writer = csv.DictWriter(fileObj, m_list[0].keys())
# 			writer.writeheader()
# 		else:
# 			print("csv.header is exit()!!!")

