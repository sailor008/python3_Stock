# -*- coding: utf-8 -*-



from utils import FileUtil




fileNameList = FileUtil.GetFileListFromFolderWithExtension("/Users/SeekMac/Code_Projects/study_python/python3_projects/stock_analyse/data", 
	False, [".csv"])
for fileName in fileNameList.values():
	print(fileName)