# -*- coding: utf-8 -*-

"""
FileName: SQLiteUtil.py
SQLite操作类
"""

# ### 枚举方法一：枚举值从 0 开始
# from enum import Enum
# SQLDataTypeEnum = Enum("SQLDataTypeEnum", ("Null", "Integer", "Real", "Text", "Blob", "Int", "Char", "Varchar", "Timestamp"))
### 枚举方法二： 通过继承 Enum 来派生枚举类，可定义复杂的枚举【装饰器unique保证没有取值重复！！！】
from enum import Enum, unique
@unique
class SQLDataTypeEnum(Enum):
    Null        = 0
    Integer     = 1 #带符号的整数，根据值大小存储在 1、2、3、4、6或8字节中
    Real        = 2 #浮点数，以8字节IEEE浮点数存放
    Text        = 3 #存储可变长度非Unicode的文本字符串，使用数据库编码（UTF-8，UTF-16BE或UTF-16LE）存储
    Blob        = 4 #不做任何转换，表示二进制大对象，用于保存图片、图像、视频等
    Int         = 5 #integer 类型，不过int不能设置主键自增！！！
    Char        = 6 #存储固定长度的字符串，长度需指定，存储效率高
    Varchar     = 7 #存储变长字符串，varchar类型的实际长度是它的值的实际长度 + 1。varchar(10) 表示不超过10个字符的数据，节省存储空间。
    DateTime    = 8  #存储日期



import sqlite3
import os

from threading import Lock

l = Lock()


class SqliteUtil():
    __instance = None

    #sqlContext
    __sqlContext = None
    __sqlCursor = None
    def __new__(cls, *args, **kwargs): 
        #线程安全 创建单例
        if not cls.__instance:
            l.acquire() #保证安全
            cls.__instance = object.__new__(cls)
            l.release() #保证安全
        return cls.__instance
    
    def __init__(self):
        pass

    def __del__(self):
        self.CloseSql()

    def ConnectSql(self, dbFilePath, isCreateNew = True):
        if not isCreateNew and not os.path.exists(dbFilePath):
            return
        print("db.path = "+dbFilePath)
        self.__sqlContext = sqlite3.connect(dbFilePath)
        self.__sqlCursor = self.__sqlContext.cursor()
        pass
    def CloseSql(self):
        if self.__sqlContext != None:
            self.__sqlContext.close()
        pass

    def CreateTable(self, tableName : str, fields : tuple):
        # CREATE TABLE tab1 (id integer primary key,name varchar(10) UNIQUE,fucktime date)
        if (type(fields) != list and type(fields) != tuple) or len(fields) <= 0 :
            print("【CreateTable】-> Error: %s fields is not tuple(string)!"%tableName)
            return
        sqlStr = "CREATE TABLE {0} ({1})".format(tableName, ", ".join(fields))
        try:
            self.__sqlCursor.execute(sqlStr)
            print("【CreateTable】-> Success! sql =  "+sqlStr)
        except BaseException as err:
            print("sqlite.except！error:", err)
        finally:
            # end logic for try!
            pass
        pass
    def InsertData(self, tableName : str, fields : tuple, data : list):
        if type(fields) != tuple or len(fields) <= 0 :
            print("【InsertData】-> Error: %s fields is not tuple(string)!"%tableName)
            return
        if (type(data) != list and type(data) != tuple) or len(data) <= 0 :
            print("【InsertData】-> Error: %s data is not list(string)!"%tableName)
            return
        valFormat = "?".ljust(len(fields), '?')
        valFormat = ",".join(valFormat)
        sqlStr = "INSERT INTO {0} {1} VALUES ({2})".format(tableName, fields, valFormat)
        try:
            # INSERT INTO tab1 ('id', 'name', 'fucktime') VALUES (?,?,?)
            self.__sqlCursor.execute(sqlStr, data) 
            self.__sqlContext.commit()
            print("【InsertData】-> Success! sql =  "+sqlStr)
        except BaseException as err:
            print("sqlite.except！error:", err)
        finally:
            # end logic for try!
            pass
        pass
    def InsertDataList(self, tableName : str, fields : tuple, data : list):
        if type(fields) != tuple or len(fields) <= 0 :
            print("【InsertDataList】-> Error: %s fields is not tuple(string)!"%tableName)
            return
        if type(data) != list or len(data) <= 0 :
            print("【InsertDataList】-> Error: %s data is not list(obj)!"%tableName)
            return
        valFormat = "?".ljust(len(fields), '?')
        valFormat = ",".join(valFormat)
        sqlStr = "INSERT INTO {0} {1} VALUES ({2})".format(tableName, fields, valFormat)
        try:
            # INSERT INTO tab1 ('id', 'name', 'fucktime') VALUES (?,?,?)
            self.__sqlCursor.executemany(sqlStr, data) 
            self.__sqlContext.commit()
            print("【InsertDataList】-> Success! sql =  "+sqlStr)
        except BaseException as err:
            print("sqlite.except！error:", err)
        finally:
            # end logic for try!
            pass
        pass
    





    
if __name__ == "__main__":
    #作为脚本直接执行会调用此处代码
    pass
