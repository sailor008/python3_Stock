# import system module
import sys
import os
root_path = os.path.abspath('.')
sys.path.append(root_path+'/utils')
sys.path.append(root_path+'/showapi')


#import custom code
import constant
import g_var
import api_func


g_var._init()#在主模块初始化全局变量的dic

# #定义跨模块全局变量
g_var.set_value('HOST','https://ali-stock.showapi.com-8')


print("main_start>>> AppKey = %s, secret = %s"%(constant.AppKey, constant.AppSecret))

api_func.request_stock_block_list()

