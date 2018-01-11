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


# import Stock_block_model
# import Stock_block_list_model

# DataManager.writeOriginalData("tesatfewagtewaew")


