#coding:utf-8
from django.http import HttpResponse,JsonResponse

# 返回json数据
def json_response(HttpStatusCode,Msg,Data):
    response_data = {}
    response_data['result'] = HttpStatusCode
    response_data['message'] = Msg
    response_data['data'] = Data
    response = HttpResponse(JsonResponse(response_data), content_type="application/json; charset=utf-8")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    response["Access-Control-Allow-Credentials"] = "true"
    return response