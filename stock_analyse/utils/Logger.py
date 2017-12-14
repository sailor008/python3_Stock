"""
log管理类
"""
import time
import os
import csv

root_path = os.path.abspath('.')
log_data_path = root_path+"/log_files/"

# #是否开启log的总开关
IsLog = True
LogLevel = 1 #注意：该参数暂未启用！

m_perLogFileSize = 4.0 * 1024 #这里的单位是kb，单个log文件的大小

# #每次开启程序时，以当前的日期创建log文件目录
m_todayDate = time.strftime('%Y%m%d', time.localtime(time.time()))
m_todayLogPath = log_data_path+m_todayDate+"/"


m_logFileObj = None
m_logFileWriter = None

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
		tag = "==>>";
	print("%s : %s \n"%(tag,msg))

def logTip(msg):
	log(msg, "Tip")

def logError(msg):
	log(msg, "Error")

def writeSingleLine(msg, tag = None):
	if not IsLog:
		return
	if tag==None:
		tag = "BaseLog";
	print("------------is log file exist???:%d" %os.path.isfile(m_todayLogPath+m_todayDate+".csv"))
	startWriteArrowLog()
	try:
		writeRowLog(msg, tag)
	finally:
		endWriteArrowLog()

def startWriteArrowLog():
	global m_logFileWriter
	m_logFileWriter = getLogFileWriter()

def writeRowLog(msg, tag = None):
	if m_logFileWriter == None:
		print("Error: log file writer is not init!!!")
		return
	if tag==None:
		tag = "BaseLog";
	timestamp = time.time()
	m_logFileWriter.writerow((timestamp, tag, msg)) 
def writeArrowLog(msgArray, tag = None):
	print("----")

def endWriteArrowLog():
	global m_logFileObj
	global m_logFileWriter
	m_logFileObj.close()
	m_logFileObj = None
	m_logFileWriter = None

def getLogFileWriter():
	global m_logFileObj
	curLogFilePath = m_todayLogPath+m_todayDate+".csv"
	fileWriter = None
	if os.path.isfile(curLogFilePath):
		m_logFileObj = open(curLogFilePath, 'a+')
		fileWriter = csv.writer(m_logFileObj)
		# fileSize = os.path.getsize(m_todayLogPath+m_todayDate+".csv")
		# print("file.size = %f kb"%(fileSize/1024))
	else:
		m_logFileObj = open(curLogFilePath, 'a+')
		# fields = ['Time', 'Tag', 'Content']
		# fileWriter = csv.DictWriter(m_logFileObj, fieldnames = fields)
		# fileWriter.writeheader()
		fileWriter = csv.writer(m_logFileObj)
		fileWriter.writerow(['Time', 'Tag', 'Content'])
	return fileWriter


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



	