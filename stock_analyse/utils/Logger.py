"""
log输出
"""
import time
import os
import csv

root_path = os.path.abspath('.')
log_data_path = root_path+"/log_files/"

# #是否开启log的总开关
IsLog = True
LogLevel = 1 #注意：该参数暂未启用！

# #每次开启程序时，以当前的日期创建log文件目录
m_todayDate = time.strftime('%Y%m%d', time.localtime(time.time()))
m_todayLogPath = log_data_path+m_todayDate+"/"

def _init():
	if not os.path.exists(log_data_path): 
		os.makedirs(log_data_path)
		print("LOG:--->>is create log_files path...")
	else:
		print("LOG:--->>log_files path is exist!!!!")

	print("LOG:--->> today log path = "+m_todayLogPath)
	if not os.path.exists(m_todayLogPath):
		os.makedirs(m_todayLogPath)

def log(msg, tag = None):
	if not IsLog:
		return
	if tag==None:
		tag = "BaseLog";
	print(""+tag+":--->> "+msg)

def writeline(msg, tag = None):
	if not IsLog:
		return
	if tag==None:
		tag = "BaseLog";
	# print("Func_write_line:"+msg)
	timestamp = time.time()
	logfile = open(m_todayLogPath+m_todayDate+".csv", 'w+') 
	try:
		writer = csv.writer(logfile) 
		writer.writerow(('Time', 'Tag', 'Content')) 
		writer.writerow((timestamp, tag, msg)) 
	finally:
		logfile.close()

	