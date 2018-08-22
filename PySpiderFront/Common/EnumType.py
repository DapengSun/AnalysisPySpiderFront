#coding:utf-8
from enum import Enum

# 请求返回状态
class ReponseCode(Enum):
    正常 = 200
    失败 = 400
    异常 = 500