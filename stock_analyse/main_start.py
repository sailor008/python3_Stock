# import system module
import sys
import os
root_path = os.path.abspath('.')
# #把模块的路径加到当前的主程序中
sys.path.append(root_path+'/utils')
sys.path.append(root_path+'/showapi')


#import custom code
import constant
import g_var
import Logger
import FileHelper

import api_func


g_var._init()#在主模块初始化全局变量的dic

# #定义当前的程序名称
g_var.set_value("ApplicationTag", "stock_analyse")
# #定义文件的根路径
g_var.set_value('DataPath', root_path+'/data')

# #定义跨模块全局变量
g_var.set_value('HOST','https://ali-stock.showapi.com-8')



# #>>>>-----初始化-----<<<<<
#注意：Logger的初始化必须比其他类早
Logger._init()
FileHelper._init()


# print("main_start>>> AppKey = %s, secret = %s"%(constant.AppKey, constant.AppSecret))

# api_func.request_stock_block_list()


Logger.writeLine("--->>>test_log565631")
