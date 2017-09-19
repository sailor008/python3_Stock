import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import os
# from urllib.request import urlretrieve 
# from urllib.request import urlopen 
# from bs4 import BeautifulSoup
import csv

import g_var
import Logger

root_path = os.path.abspath('.')
LOG_TAG = "FileHelper"

def _init():
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

def create_file(fileName):
	Logger.log("is c", LOG_TAG)
