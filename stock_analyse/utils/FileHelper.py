"""
FileName: FileHelper.py
文件操作类
"""
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# from urllib.request import urlretrieve 
# from urllib.request import urlopen 
# from bs4 import BeautifulSoup

import os
import csv

import g_var
import Logger

LOG_TAG = "FileHelper"
application_path = g_var.get_value("applicationPath")


def _init():
	Logger.log("is FileHelper.init()")

# 【注意：相同的文件名，在不同的目录下，后续优化给出警告的提示！】
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

def get_title_rows(jsonListData):
    title = []
    row_num = 0
    rows=[]
    for key in jsonListData:
        title.append(key)
        v = jsonListData[key]
        if len(v)>row_num:
            row_num = len(v)
        continue
    for i in range(row_num):
        row = {}
        for k in jsonListData:
            v = jsonListData[k]
            if i in v.keys():
                row[k]=v[i]
            else:
                row[k] = ''
        rows.append(row)
    return title, rows

# 后续需要处理文件的操作权限！！！
def createFile(filePath):
	Logger.log("is create file = %s"%filePath, LOG_TAG)
	open(filePath, "w")

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
