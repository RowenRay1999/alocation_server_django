import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from django.http.response import JsonResponse

from common.models import User


# user登录
@api_view(["GET", "POST"])
def user_login(request):
    if request.method == "GET":
        return JsonResponse(
            {"message": "get test"}, safe=False, status=status.HTTP_200_OK
        )
    elif request.method == "POST":
        json_str = request.body
        json_dict = json.loads(json_str)
        account = json_dict.get("account", None)
        resultObj = User()
        resultObj.user_account = int(account)
        print(account)
        return JsonResponse(
            {"message": resultObj.user_account}, safe=False, status=status.HTTP_200_OK
        )


# 用户注册
@api_view(["GET", "POST"])
def user_register(request):
    if request.method == "GET":
        return JsonResponse(
            {"message": "get test"}, safe=False, status=status.HTTP_200_OK
        )


# 用户退出登录
@api_view(["GET", "POST"])
def user_logout(request):
    if request.method == "GET":
        return JsonResponse(
            {"message": "get test"}, safe=False, status=status.HTTP_200_OK
        )


# 忘记密码
@api_view(["GET", "POST"])
def user_forget_pwd_client(request):
    if request.method == "GET":
        return JsonResponse(
            {"message": "get test"}, safe=False, status=status.HTTP_200_OK
        )


# 用户信息变更
@api_view(["GET", "POST"])
def user_update_client(request):
    if request.method == "GET":
        return JsonResponse(
            {"message": "get test"}, safe=False, status=status.HTTP_200_OK
        )


# 用户数据获取
@api_view(["GET", "POST"])
def user_data_client(request):
    if request.method == "GET":
        return JsonResponse(
            {"message": "get test"}, safe=False, status=status.HTTP_200_OK
        )


# 用户信息获取
@api_view(["GET", "POST"])
def user_base_client(request):
    if request.method == "GET":
        return JsonResponse(
            {"message": "get test"}, safe=False, status=status.HTTP_200_OK
        )


# 用户数据变更
@api_view(["GET", "POST"])
def user_data_update_client(request):
    if request.method == "GET":
        return JsonResponse(
            {"message": "get test"}, safe=False, status=status.HTTP_200_OK
        )
