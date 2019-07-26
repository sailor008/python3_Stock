# -*- coding: utf-8 -*-

import os
import re



file_exclude_patterns = [
	"*.gitignore",
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
	".DS_Store",
	"*.class",
	"*.psd",
	"*.db",
	"*.sublime-workspace",
	".svn",
]


#####获取path目录下的文件列表########
def GetFileListFromPath(path, isRecursive = False, ignoreFileExteDic = file_exclude_patterns):
	print("is ignoreFileExteDic-------------")

GetFileListFromPath("testPath")