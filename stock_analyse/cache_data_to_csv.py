import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import os
# from urllib.request import urlretrieve 
# from urllib.request import urlopen 
# from bs4 import BeautifulSoup
import csv

tmpPath = "data"
if not os.path.exists(tmpPath): 
	os.makedirs(tmpPath)
	print("is create path..")
else:
	print("file is exist!!!!")


csvFile = open("data/stock_block.csv", 'w+') 
try:
	writer = csv.writer(csvFile) 
	writer.writerow(('number', 'number plus 2', 'number times 2')) 
	for i in range(20):
		writer.writerow( (i, i+2, i*2)) 
finally:
	csvFile.close()

