"""
@File: cache.py
@time: 2020/11/3 5:43 上午
@Version: python3.8
@Author: Leilei Chui
@Contact: leilei.chui@gmail.com
@License: MIT Licence 
@Software: PyCharm
"""
import redis

redis_addr = {
    "host": 'localhost',
    "port": 6379
}


class Cache:
    def __init__(self):
        self.online_cache = redis.StrictRedis(**redis_addr, db=0, decode_responses=True)

    def set(self, name, json_data):
        for key in json_data.keys():
            self.online_cache.hset(name, key, json_data[key])

    def get(self, name, key):
        return self.online_cache.hget(name, key)


cache = Cache()
if __name__ == '__main__':
    cache.set('uid', {
        "filed": "测试"
    })
    value = cache.get('uid', 'filed')
    print(value)
