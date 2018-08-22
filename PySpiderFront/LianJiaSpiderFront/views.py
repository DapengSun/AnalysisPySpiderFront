#coding:utf-8
import json

import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from Common.Reponse import json_response
from Common.EnumType import ReponseCode

import PySpiderFront


def searchindex(request):
    return render(request,'index.html')

@require_http_methods(["POST"])
@csrf_exempt
def pushjobinqueue(request):
    try:
        # 获取请求参数
        _spiderContent = request.POST.get('SearchContent',None)

        _apiUrl = r'http://47.93.244.255:8085/lianjia/ershoufang/api/pushjobqueue'
        _spiderUrl = r'https://bj.lianjia.com/ershoufang/rs%s' % (_spiderContent)

        _data = {
            "searchSpider" : _spiderUrl
        }
        _response = requests.post(_apiUrl,data=json.dumps(_data))
        _responseJson = json.loads(_response.text)

        # print(_responseJson)

        if _responseJson['result'] == ReponseCode.正常.value:
            return json_response(ReponseCode.正常.value,"检索内容已加入分析列表！",'')
        else:
            return json_response(ReponseCode.失败, "检索内容已加入分析列表失败！", _responseJson.message)
    except Exception as ex:
        return json_response(ReponseCode.失败, "检索内容已加入分析列表异常！", ex.message)