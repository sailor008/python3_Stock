"""
FileName: NetworkMgr.py
network管理类
"""
import urllib, sys
import ssl
import json

import constant
import Logger

m_ctx = ssl.create_default_context()
m_ctx.check_hostname = False
m_ctx.verify_mode = ssl.CERT_NONE

# return dic data for json
# 【注意：需要处理网络连接失败的逻辑】
def requestURLWithGet(url, successBlock = None, failureBlock = None):
	global m_ctx

	bodys = {}
	method = 'GET'
	# 拼接url
	Logger.log("now request.url = "+url)

	request = urllib.request.Request(url)
	request.add_header('Authorization', 'APPCODE ' + constant.AppCode)
	response = urllib.request.urlopen(request, context=m_ctx)
	respData = response.read()
	if (respData):
		Logger.logTip("connect success! 返回的数据如下：\n %s"%respData)
		jsonAttrs = json.loads(respData)
		if jsonAttrs.get("showapi_res_code")!=None and jsonAttrs.get("showapi_res_code") == 0:
			Logger.logTip("getRequest success! url = [%s]"%url)
			bodyData = jsonAttrs.get("showapi_res_body")
			if(successBlock):
				successBlock(bodyData)
		else:
			errorMsg = jsonAttrs.get("showapi_res_error")
			Logger.logError("url respone errorcode! ErrorMsg = %s"%errorMsg)
			if(failureBlock):
				failureBlock(errorMsg)
	else:
		Logger.logError("网络链接错误！url = %s" %url)

