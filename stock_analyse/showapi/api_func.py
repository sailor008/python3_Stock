# import system module
import urllib, sys
from urllib import request
import ssl


# import custom code
import constant
import g_var


def request_stock_block_list():
	print("start print the result of GET stock-block-list: "+ g_var.get_value('HOST'))

	host = 'https://ali-stock.showapi.com'
	path = '/stock-block-list'
	method = 'GET'
	appcode = '你自己的AppCode'
	querys = ''
	bodys = {}
	url = host + path

	# request = request.Request(url)
	# request.add_header('Authorization', 'APPCODE ' + appcode)
	# ctx = ssl.create_default_context()
	# ctx.check_hostname = False
	# ctx.verify_mode = ssl.CERT_NONE
	# response = request.urlopen(request, context=ctx)
	# content = response.read()
	# if (content):
	# 	print("start print the result of GET stock-block-list: ")
	#     print(content)

