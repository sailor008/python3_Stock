"""
FileName: FileHelper.py
文件操作类
"""
import sys
import os

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# from urllib.request import urlretrieve 
# from urllib.request import urlopen 
# from bs4 import BeautifulSoup
import csv

import g_var
import Logger

root_path = os.path.abspath('.')
LOG_TAG = "FileHelper"

m_globalFileDic = {}

def _init():
	initDataFileDic()

def initDataFileDic():
	#使用的全局变量.begin:
	global m_globalFileDic
	#使用的全局变量.end
	data_path = g_var.get_value('DataPath')
	if not os.path.exists(data_path): 
		os.makedirs(data_path)
		Logger.log("create path【data】...", LOG_TAG)
		return
	Logger.log("【data】path is exist!!!! \n\n\n", LOG_TAG)
	m_globalFileDic = getFileList("/Users/SeekMac/Code_Projects/study_python/python_projects/stock_analyse")
	print("目录的总数 = %d"%len(m_globalFileDic.keys()))
	for keystr, val in m_globalFileDic.items():
		print("------>>> %s : %s \n" %(keystr,val))
	print("Tip: DataFileDic init success!")

def getFileList(targetPath, recursiveCount = -1, ignoreFileExteDic = {'.pyc','.DS_Store','.gitignore','.svn'}):
	fileList = {}
	if(not os.path.isdir(targetPath)):
		print("Error:【%s】 is just a file. not a dir path!!!"%targetPath)
		return
	tempPathList = [targetPath]
	tempRecursiveDic = {targetPath:0}
	while len(tempPathList) > 0:
		curPath = tempPathList[0]
		del tempPathList[0]
		if recursiveCount > 0 and tempRecursiveDic[curPath] >= recursiveCount:
			break
		print("当前查询的目录：%s"%curPath)
		tempNameList = os.listdir(curPath)
		for pathName  in tempNameList:
			fullPath = curPath + "/" + pathName
			if(os.path.isfile(fullPath)):
				# 【注意：此处需要在windows 测试去除文件扩展名的情况】
				fileNameInfo = os.path.splitext(pathName)
				# 取出文件的扩展名
				fileExtension = fileNameInfo[0]
				if (len(fileNameInfo) > 1 and len(fileNameInfo[1]) > 1):
					fileExtension = fileNameInfo[1]
				if fileExtension not in ignoreFileExteDic:
					fileList[pathName] = fullPath
				else:
					print("------------该文件即将被忽略："+pathName)
			else:
				print("--------fullPath = %s"%fullPath)
				tempPathList.append(fullPath)
				tempRecursiveDic[fullPath] = tempRecursiveDic[curPath] + 1
	return fileList


def create_file(fileName):
	Logger.log("is c", LOG_TAG)
def deleteFile(fileName):
	Logger.log("deleteFile.name = "+fileName)

def saveListDataToCSV(fileName, listData):
	print("is saveListDataToCSV")


def saveData(fileName, listData):
	data_path = g_var.get_value('DataPath')
	if not os.path.exists(data_path): 
		os.makedirs(data_path)
		Logger.log("create path【data】...", LOG_TAG)
	else:
		Logger.log("【data】path is exist!!!!", LOG_TAG)

	csvFile = open(data_path+"/stock_block.csv", 'w+') 
	try:
		writer = csv.writer(csvFile) 
		writer.writerow(('number', 'number plus 2', 'number times 2')) 
		for i in range(20):
			writer.writerow( (i, i+2, i*2)) 
	finally:
		csvFile.close()
