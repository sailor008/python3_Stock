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

m_perLogFileSize = 4.0 #这里的单位是M（兆），单个log文件的大小

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

def writeLine(msg, tag = None):
	if not IsLog:
		return
	if tag==None:
		tag = "BaseLog";
	print("------------is log file exist???:%d" %os.path.isfile(m_todayLogPath+m_todayDate+".csv"))
	fileSize = os.path.getsize(m_todayLogPath+m_todayDate+".csv")
	print("file.size = %f kb"%(fileSize/1024))
	timestamp = time.time()
	logfile = open(m_todayLogPath+m_todayDate+".csv", 'a+') 
	try:
		writer = csv.writer(logfile) 
		writer.writerow(('Time', 'Tag', 'Content')) 
		writer.writerow((timestamp, tag, msg)) 
	finally:
		logfile.close()


def func_replaceFileWithData(file, data):
	log("is func_replaceFileWithData-->>>")

def func_appendDataToFile(file, data):
	log("is func_appendDataToFile-->>>")

def func_readFileData(file, data):
	log("is func_readFileData-->>>")

def func_deleteFile(file, data):
	log("is func_deleteFile-->>>")

def func_clearFileData(file, data):
	log("is func_clearFileData-->>>")



	