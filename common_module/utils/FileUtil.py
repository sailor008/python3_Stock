# -*- coding: utf-8 -*-

"""
FileName: FileUtil.py
文件工具类
"""

import os
import re



file_exclude_patterns = [
	"*.meta",
	"*.pyc",
	"*.pyo",
	"*.exe",
	"*.dll",
	"*.obj",
	"*.o",
	"*.a",
	"*.lib",
	"*.so",
	"*.dylib",
	"*.ncb",
	"*.sdf",
	"*.suo",
	"*.pdb",
	"*.idb",
	"*.class",
	"*.db",
	"*.sublime-workspace",
	"*.gitignore",
	#下面为mac下的文件名
	".gitignore",
	".gitattributes",
	".svn",
	".DS_Store",
]


#####获取path目录下的文件列表########
def GetFileListFromFolder(folderPath, isRecursive = False, ignoreFileExteDic = file_exclude_patterns):
	if not os.path.isdir(folderPath):
		print("Error: the path【%s】 is not the dir!!!"%path)
		return None
	fileNameList = {}
	for entry in os.scandir(folderPath):
		if entry.is_file():
			if entry.name.startswith("."):  ###过滤掉mac下特定的默认文件, 例如 【.DS_Store】
				continue
			fileExtension = os.path.splitext(entry.name)[-1] ###提取文件的扩展名###
			if fileExtension not in ignoreFileExteDic:
				fileNameList[len(fileNameList)] = entry.name
			else:
				print("过滤该文件："+entry.name)
				pass
	return fileNameList


####获取folderPath 目录下的特定扩展名的文件列表######
def GetFileListFromFolderWithExtension(folderPath, isRecursive = False, targetExtensionList = None):
	if not os.path.isdir(folderPath):
		print("Error: the path【%s】 is not the dir!!!"%path)
		return None
	if targetExtensionList != None and type(targetExtensionList) != list:
		print("Error: the file target extension is except type(dir)!!!")
		return None
	fileNameList = {}
	for entry in os.scandir(folderPath):
		if entry.is_file():
			if entry.name.startswith("."):  ###过滤掉mac下特定的默认文件, 例如 【.DS_Store】
				continue
			fileExtension = os.path.splitext(entry.name)[-1] ###提取文件的扩展名###
			if fileExtension in targetExtensionList:
				fileNameList[len(fileNameList)] = entry.name
			else:
				print("过滤该文件："+entry.name)
				pass
	return fileNameList












