"""
FileName: NetworkMgr.py
network管理类
"""
import urllib, sys
import ssl
import json

import constant
import Logger
import DataManager

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
	# respData = "{\"showapi_res_code\":0,\"showapi_res_error\":\"\",\"showapi_res_body\":{\"ret_code\":0,\"list\":[{\"trade_money\":\"368947118.000\",\"diff_money\":\"-0.03\",\"open_price\":\"8.880\",\"code\":\"601006\",\"date\":\"2017-11-30\",\"min_price\":\"8.810\",\"market\":\"sh\",\"trade_num\":\"416807\",\"turnover\":\"0.280\",\"close_price\":\"8.850\",\"max_price\":\"8.910\",\"swing\":\"1.13\",\"diff_rate\":\"-0.34\"},{\"trade_money\":\"388937580.000\",\"diff_money\":\"-0.02\",\"open_price\":\"8.900\",\"code\":\"601006\",\"date\":\"2017-11-29\",\"min_price\":\"8.820\",\"market\":\"sh\",\"trade_num\":\"438484\",\"turnover\":\"0.295\",\"close_price\":\"8.880\",\"max_price\":\"8.920\",\"swing\":\"1.12\",\"diff_rate\":\"-0.22\"},{\"trade_money\":\"338012785.000\",\"diff_money\":\"-0.12\",\"open_price\":\"8.940\",\"code\":\"601006\",\"date\":\"2017-11-28\",\"min_price\":\"8.870\",\"market\":\"sh\",\"trade_num\":\"379584\",\"turnover\":\"0.255\",\"close_price\":\"8.900\",\"max_price\":\"8.970\",\"swing\":\"1.11\",\"diff_rate\":\"-1.33\"},{\"trade_money\":\"679468677.000\",\"diff_money\":\"0.0\",\"open_price\":\"8.940\",\"code\":\"601006\",\"date\":\"2017-11-27\",\"min_price\":\"8.790\",\"market\":\"sh\",\"trade_num\":\"762013\",\"turnover\":\"0.513\",\"close_price\":\"9.020\",\"max_price\":\"9.040\",\"swing\":\"2.77\",\"diff_rate\":\"0.0\"},{\"trade_money\":\"716821338.000\",\"diff_money\":\"-0.09\",\"open_price\":\"9.060\",\"code\":\"601006\",\"date\":\"2017-11-24\",\"min_price\":\"8.810\",\"market\":\"sh\",\"trade_num\":\"801930\",\"turnover\":\"0.539\",\"close_price\":\"9.020\",\"max_price\":\"9.100\",\"swing\":\"3.18\",\"diff_rate\":\"-0.99\"},{\"trade_money\":\"1061585849.000\",\"diff_money\":\"-0.27\",\"open_price\":\"9.400\",\"code\":\"601006\",\"date\":\"2017-11-23\",\"min_price\":\"9.030\",\"market\":\"sh\",\"trade_num\":\"1141401\",\"turnover\":\"0.768\",\"close_price\":\"9.110\",\"max_price\":\"9.490\",\"swing\":\"4.9\",\"diff_rate\":\"-2.88\"},{\"trade_money\":\"930883985.000\",\"diff_money\":\"0.09\",\"open_price\":\"9.310\",\"code\":\"601006\",\"date\":\"2017-11-22\",\"min_price\":\"9.210\",\"market\":\"sh\",\"trade_num\":\"1001580\",\"turnover\":\"0.674\",\"close_price\":\"9.380\",\"max_price\":\"9.390\",\"swing\":\"1.94\",\"diff_rate\":\"0.97\"},{\"trade_money\":\"1164999730.000\",\"diff_money\":\"0.26\",\"open_price\":\"9.000\",\"code\":\"601006\",\"date\":\"2017-11-21\",\"min_price\":\"8.960\",\"market\":\"sh\",\"trade_num\":\"1268321\",\"turnover\":\"0.853\",\"close_price\":\"9.290\",\"max_price\":\"9.350\",\"swing\":\"4.32\",\"diff_rate\":\"2.88\"},{\"trade_money\":\"471383497.000\",\"diff_money\":\"0.0\",\"open_price\":\"9.000\",\"code\":\"601006\",\"date\":\"2017-11-20\",\"min_price\":\"8.890\",\"market\":\"sh\",\"trade_num\":\"525579\",\"turnover\":\"0.354\",\"close_price\":\"9.030\",\"max_price\":\"9.060\",\"swing\":\"1.88\",\"diff_rate\":\"0.0\"},{\"trade_money\":\"971205411.000\",\"diff_money\":\"0.24\",\"open_price\":\"8.800\",\"code\":\"601006\",\"date\":\"2017-11-17\",\"min_price\":\"8.700\",\"market\":\"sh\",\"trade_num\":\"1093673\",\"turnover\":\"0.736\",\"close_price\":\"9.030\",\"max_price\":\"9.060\",\"swing\":\"4.1\",\"diff_rate\":\"2.73\"},{\"trade_money\":\"285205565.000\",\"diff_money\":\"-0.12\",\"open_price\":\"8.890\",\"code\":\"601006\",\"date\":\"2017-11-16\",\"min_price\":\"8.780\",\"market\":\"sh\",\"trade_num\":\"323445\",\"turnover\":\"0.218\",\"close_price\":\"8.790\",\"max_price\":\"8.890\",\"swing\":\"1.23\",\"diff_rate\":\"-1.35\"},{\"trade_money\":\"352421722.000\",\"diff_money\":\"-0.04\",\"open_price\":\"8.930\",\"code\":\"601006\",\"date\":\"2017-11-15\",\"min_price\":\"8.830\",\"market\":\"sh\",\"trade_num\":\"396352\",\"turnover\":\"0.267\",\"close_price\":\"8.910\",\"max_price\":\"8.960\",\"swing\":\"1.45\",\"diff_rate\":\"-0.45\"},{\"trade_money\":\"272978108.000\",\"diff_money\":\"-0.04\",\"open_price\":\"9.000\",\"code\":\"601006\",\"date\":\"2017-11-14\",\"min_price\":\"8.910\",\"market\":\"sh\",\"trade_num\":\"304990\",\"turnover\":\"0.205\",\"close_price\":\"8.950\",\"max_price\":\"9.010\",\"swing\":\"1.11\",\"diff_rate\":\"-0.44\"},{\"trade_money\":\"371140472.000\",\"diff_money\":\"0.15\",\"open_price\":\"8.840\",\"code\":\"601006\",\"date\":\"2017-11-13\",\"min_price\":\"8.820\",\"market\":\"sh\",\"trade_num\":\"415312\",\"turnover\":\"0.279\",\"close_price\":\"8.990\",\"max_price\":\"9.020\",\"swing\":\"2.26\",\"diff_rate\":\"1.7\"},{\"trade_money\":\"332588918.000\",\"diff_money\":\"-0.08\",\"open_price\":\"8.920\",\"code\":\"601006\",\"date\":\"2017-11-10\",\"min_price\":\"8.790\",\"market\":\"sh\",\"trade_num\":\"376272\",\"turnover\":\"0.253\",\"close_price\":\"8.840\",\"max_price\":\"8.930\",\"swing\":\"1.57\",\"diff_rate\":\"-0.9\"},{\"trade_money\":\"241490411.000\",\"diff_money\":\"0.04\",\"open_price\":\"8.870\",\"code\":\"601006\",\"date\":\"2017-11-09\",\"min_price\":\"8.850\",\"market\":\"sh\",\"trade_num\":\"271364\",\"turnover\":\"0.183\",\"close_price\":\"8.920\",\"max_price\":\"8.930\",\"swing\":\"0.9\",\"diff_rate\":\"0.45\"},{\"trade_money\":\"377205964.000\",\"diff_money\":\"0.02\",\"open_price\":\"8.860\",\"code\":\"601006\",\"date\":\"2017-11-08\",\"min_price\":\"8.830\",\"market\":\"sh\",\"trade_num\":\"424379\",\"turnover\":\"0.285\",\"close_price\":\"8.880\",\"max_price\":\"8.960\",\"swing\":\"1.47\",\"diff_rate\":\"0.23\"},{\"trade_money\":\"404532369.000\",\"diff_money\":\"0.03\",\"open_price\":\"8.820\",\"code\":\"601006\",\"date\":\"2017-11-07\",\"min_price\":\"8.780\",\"market\":\"sh\",\"trade_num\":\"457014\",\"turnover\":\"0.307\",\"close_price\":\"8.860\",\"max_price\":\"8.900\",\"swing\":\"1.36\",\"diff_rate\":\"0.34\"},{\"trade_money\":\"326183604.000\",\"diff_money\":\"-0.01\",\"open_price\":\"8.840\",\"code\":\"601006\",\"date\":\"2017-11-06\",\"min_price\":\"8.760\",\"market\":\"sh\",\"trade_num\":\"370228\",\"turnover\":\"0.249\",\"close_price\":\"8.830\",\"max_price\":\"8.860\",\"swing\":\"1.13\",\"diff_rate\":\"-0.11\"},{\"trade_money\":\"606428072.000\",\"diff_money\":\"-0.1\",\"open_price\":\"8.940\",\"code\":\"601006\",\"date\":\"2017-11-03\",\"min_price\":\"8.720\",\"market\":\"sh\",\"trade_num\":\"685665\",\"turnover\":\"0.461\",\"close_price\":\"8.840\",\"max_price\":\"8.950\",\"swing\":\"2.57\",\"diff_rate\":\"-1.12\"},{\"trade_money\":\"322562461.000\",\"diff_money\":\"0.03\",\"open_price\":\"8.920\",\"code\":\"601006\",\"date\":\"2017-11-02\",\"min_price\":\"8.840\",\"market\":\"sh\",\"trade_num\":\"361503\",\"turnover\":\"0.243\",\"close_price\":\"8.940\",\"max_price\":\"8.980\",\"swing\":\"1.57\",\"diff_rate\":\"0.34\"},{\"trade_money\":\"682116475.000\",\"diff_money\":\"-0.19\",\"open_price\":\"9.100\",\"code\":\"601006\",\"date\":\"2017-11-01\",\"min_price\":\"8.890\",\"market\":\"sh\",\"trade_num\":\"760051\",\"turnover\":\"0.511\",\"close_price\":\"8.910\",\"max_price\":\"9.100\",\"swing\":\"2.31\",\"diff_rate\":\"-2.09\"}]}}"
	if (respData):
		DataManager.writeOriginalData(respData)
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

