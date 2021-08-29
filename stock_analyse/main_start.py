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


import TuShare_api




# #>>>>-----初始化-----<<<<<
#注意：Logger的初始化必须比其他类早
Logger._init()
FileHelper._init()
DataManager._init()


# print("main_start>>> AppKey = %s, secret = %s"%(constant.AppKey, constant.AppSecret))

# api_func.request_stock_block_list()


# Logger.writeLineLog("--->>>test_log565631", None)


# import Stock_block_model
# import Stock_block_list_model
# DataManager.writeOriginalData("tesatfewagtewaew")




# TuShare_api.GetOneStockDaily("301000.SZ", "20210520", "20210601")
# TuShare_api.GetOneStockBasic("301000.SZ")




# from SqliteUtil import SqliteUtil
# from SqliteUtil import SQLDataTypeEnum
from utils.SqliteUtil import *


m_dataPath = g_var.get_value('DataPath')
testDb = m_dataPath+os.path.sep + "test.db"
tableName = "tab1"
SqliteUtil().ConnectSql(testDb)
SqliteUtil().CreateTable(tableName, [
    "id integer primary key", 
    "name varchar(10) UNIQUE", 
    "fucktime datetime",
])
SqliteUtil().InsertDataList(tableName, ("id", "name", "fucktime"), [[1, "fuck001", "2021-05-21"], [2, "fuck002", "2021-05-21"]])
# SqliteUtil().CloseSql()







if __name__ == "__main__":
    #作为脚本直接执行会调用此处代码
    pass







# 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