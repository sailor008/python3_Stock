"""
FileName: NetworkMgr.py
network管理类
"""
import urllib, sys
import ssl

import constant

m_ctx = ssl.create_default_context()
m_ctx.check_hostname = False
m_ctx.verify_mode = ssl.CERT_NONE

# return dic data for json
# 【注意：需要处理网络连接失败的逻辑】
def requestDataByGet(apiUrl, strParam = None):
	global m_ctx

	bodys = {}
	method = 'GET'
	# 拼接url
	url = apiUrl
	if(strParam != None and len(strParam) > 0):
		url = url + '?' + strParam
	print("now request.url = "+url)

	request = urllib.request.Request(url)
	request.add_header('Authorization', 'APPCODE ' + constant.AppCode)
	response = urllib.request.urlopen(request, context=m_ctx)
	respData = response.read()
	if (respData):
		print("查询的结果如下：\n")
		print(respData)
		return respData
	return

