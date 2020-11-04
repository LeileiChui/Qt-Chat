"""
@File: utils.py
@time: 2020/11/4 9:32 下午
@Version: python3.8
@Author: Leilei Chui
@Contact: leilei.chui@gmail.com
@License: MIT Licence 
@Software: PyCharm
"""
import hashlib
import time


def cal_session(uid):
    byte_str = f'{uid}{int(time.time())}'.encode()
    return hashlib.md5(byte_str).hexdigest()
