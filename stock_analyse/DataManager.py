"""
FileName: DataManager.py
数据管理器
"""
import sys
import os

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import csv
import codecs

#global custom code
import g_var
import Logger
import FileHelper

LOG_TAG = "DataManager"
m_dataPath = g_var.get_value('DataPath')
m_originalDataPath = m_dataPath+"/originalData"

m_globalDataFileDic = {}

def _init():
	Logger.log("is DataManager.init()")
	initDataFileDic()

def initDataFileDic():
	#使用的全局变量.begin:
	global m_globalDataFileDic
	#使用的全局变量.end
	if not os.path.exists(m_dataPath): 
		os.makedirs(m_dataPath)
		Logger.log("create path【data】...", LOG_TAG)
		return
	Logger.log("【data】path is exist!!!! \n\n\n", LOG_TAG)
	m_globalDataFileDic = FileHelper.getFileList(m_dataPath)
	print("data文件的总数 = %d"%len(m_globalDataFileDic.keys()))
	for keystr, val in m_globalDataFileDic.items():
		Logger.log("------>>> %s : %s \n" %(keystr,val), LOG_TAG)
	print("Tip: DataFileDic init success!")

def createCSVFile(fileName, headerKeys):
	filePath = "%s/%s"%(m_dataPath, fileName)
	fileObj = open(filePath, "w")
	fileWriter = csv.DictWriter(fileObj, fieldnames = headerKeys)
	fileWriter.writeheader()
	m_globalDataFileDic[fileName] = filePath

def saveJsonDataToFile(fileName, jsonData, fileType="csv"):
	if fileType == "csv":
		saveListDataToCSV(fileName, jsonData)
	else:
		saveListDataToSQLite(fileName, jsonData)

def saveListDataToCSV(fileName, listData):
	print("is saveListDataToCSV, list.count = %d"%len(listData))
	if not fileName in m_globalDataFileDic:
		headerKeys = listData[0].keys()
		createCSVFile(fileName, headerKeys)
	filePath = "%s/%s"%(m_dataPath, fileName)
	fileObj = open(filePath, "a", encoding='utf-8') 
	# fileObj = open(filePath, "a", encoding='gbk') #excel能够正确识别用gb2312、gbk、gb18030或utf_8 with BOM 编码的中文，如果是utf_8 no BOM编码的中文文件，excel打开会乱码。
	csvWriter = csv.writer(fileObj)
	for itemData in listData:
		csvWriter.writerow(itemData.values())
	# fileObj.flush()   #【注意：此行代码只用于记录，不会实际开启使用！】内存缓存直接映射至结果文件，不关闭文件情况下输出缓存至磁盘
	fileObj.close()

def saveListDataToSQLite(fileName, listData):
	print("------------is.Func: saveListDataToSQLite()")

def readOriginalDataFile(fileName):
	filePath = "%s/%s"%(m_originalDataPath, fileName)
	if not os.path.exists(filePath):
		Logger.logError("【%s】该文件不存在！"%filePath)
		return
	Logger.log("读取文件的数据，filePath = %s"%filePath)
	fileObj = open(filePath, "r", encoding='utf-8')
	fileData = fileObj.read()
	fileObj.close()
	return fileData	