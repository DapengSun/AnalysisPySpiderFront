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

        data = {
            "searchSpider" : _spiderUrl
        }

        response = requests.post(_apiUrl,data=json.dumps(data))

        return json_response(ReponseCode.正常.value,"检索内容已加入分析列表！",'')
    except Exception as ex:
        print(ex)