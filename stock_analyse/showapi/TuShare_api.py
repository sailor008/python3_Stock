"""
FileName: TuShare_api.py
TuShare的api调用封装
"""

import NetworkMgr



exportFields_stock_basic = [
    "ts_code",
    "symbol",
    "name",
    "area",
    "industry",
    "fullname",
    "enname",
    "cnspell",
    "market",
    "exchange",
    "curr_type",
    "list_date",
    "is_hs",
]
exportFields_stock_basic = ", ".join(exportFields_stock_basic)
def GetOneStockBasic(stockCode):
    return NetworkMgr.SendRequest_API_TuShare("stock_basic", exportFields_stock_basic, ts_code = stockCode)
# return data example:
# [
#       ['301000.SZ', '301000', '肇民科技', '上海', '塑料', '上海肇民新材料科技股份有限公司', 'Shanghai Hajime Advanced Material Technology Co., Ltd', 'zmkj', '创业板', 'SZSE', 'CNY', '20210528', 'N']
# ]




exportFields_daily = [
    "ts_code",
    "trade_date",
    "open",
    "high",
    "low",
    "close",
    "pre_close",
    "change",
    "pct_chg",
    "vol",
    "amount",
]
exportFields_daily = ", ".join(exportFields_daily)
def GetOneStockDaily(stockCode, startDateStr = "20210101", endDateStr = "20210102"):
    NetworkMgr.SendRequest_API_TuShare("daily", exportFields_daily, ts_code = stockCode, start_date = startDateStr, end_date=endDateStr)
# return data example:
# [
#     ['301000.SZ', '20210601', 83.5, 84.9, 82.11, 82.41, 85.04, -2.63, -3.0927, 29251.2, 242755.895], 
#     ['301000.SZ', '20210531', 87.0, 91.0, 82.03, 85.04, 94.01, -8.97, -9.5415, 46917.77, 401906.894], 
#     ['301000.SZ', '20210528', 110.0, 115.0, 93.52, 94.01, 64.31, 29.7, 46.1826, 66365.52, 670727.415]
# ]