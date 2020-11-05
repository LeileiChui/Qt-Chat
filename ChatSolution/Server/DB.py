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

    def getFriends(self, uid):
        sql = """SELECT user.uid, user.nick_name, user.avatar
FROM person_relation
         join user on user.uid = person_relation.another_uid
where person_relation.a_uid = """ + str(uid)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def getGroups(self, uid):
        sql = """SELECT `group`.g_id, `group`.g_name, `group`.g_creat_time, `group`.g_author_id, group_relation.g_nick_name
from `group`
         JOIN group_relation ON group_relation.group_id = `group`.g_id
where group_relation.uid = """ + str(uid)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        print(res)
        return res

    def getUserInfo(self, uid):
        sql = """select uid, nick_name, avatar
from user
where uid = """ + str(uid)
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        print(res)
        return res


if __name__ == '__main__':
    db = DB()
    db.getUserInfo('12345')
