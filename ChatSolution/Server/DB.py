"""
@File: DB.py
@time: 2020/11/4 8:55 下午
@Version: python3.8
@Author: Leilei Chui
@Contact: leilei.chui@gmail.com
@License: MIT Licence 
@Software: PyCharm
"""
import pymysql
import config
from protobuf.DataPack_pb2 import *
from cache import cache


class DB:
    def __init__(self):
        self.IMDB = pymysql.connect(*config.dbConfig)
        self.cursor = self.IMDB.cursor()

    def login(self, uid, password):
        sql = "SELECT * FROM user where uid={0} and password={1}".format(uid, password)
        res = self.cursor.execute(sql)
        return res == 1


if __name__ == '__main__':
    db = DB()
    db.login('10000', '123456')
