import json
from MySQLdb import IntegrityError
import bcrypt
from rest_framework import status
from rest_framework.decorators import api_view
from django.http.response import JsonResponse

from common.models import User
from common.utils import assign_user_id, check_password, gen_password
from user.forms import RegistrationForm
from user.response import errMsg
from .managers import LoginStatusManager


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
        password = json_dict.get("password", None)
        single_record = User.objects.get(pk=account)
        if check_password(password, single_record.user_password):
            resultObj = User()
            resultObj.user_account = int(account)
            print(account)
            return JsonResponse(
                {
                    "loginStatus": 100,
                    "session": LoginStatusManager.set_user_logged_in(account),
                    "expire": 3600 * 24 * 30,
                },
                safe=False,
                status=status.HTTP_200_OK,
            )
        else:
            return JsonResponse(
                {"loginStatus": 104}, safe=False, status=status.HTTP_200_OK
            )


# 用户注册
@api_view(["GET", "POST"])
def user_register(request):
    if request.method == "GET":
        return JsonResponse(
            {"message": "get test"}, safe=False, status=status.HTTP_200_OK
        )
    elif request.method == "POST":
        json_str = request.body
        json_dict = json.loads(json_str).get("formData")
        registerStatus = 100
        if json_dict is not None:
            user_instance = User()
            assign_user_id(user_instance)
            user_instance.user_account_type = int(json_dict.get("accountType"))
            user_instance.user_phone = json_dict.get("phone")
            user_instance.user_email = json_dict.get("email")
            user_instance.user_wx_info = json_dict.get("wxInfo")
            user_instance.user_password = gen_password(json_dict.get("password")).decode('utf-8')
            user_instance.user_name = json_dict.get("name")
            user_instance.user_real_info = json_dict.get("realInfo")
            user_instance.user_real_status = int(json_dict.get("realStatus"))
            user_instance.user_privilege = 1
            user_instance.user_extend = json_dict.get("extend")
            try:
                user_instance.save()
            except IntegrityError as e:
                registerStatus = 104
            err = errMsg(200, "normal").to_json()
            print(err)
            return JsonResponse(
                {
                    "registerStatus": registerStatus,
                    "account": user_instance.user_account,
                    "errorMsg": json.loads(err),
                },
                safe=False,
                status=status.HTTP_200_OK,
            )
        else:
            return JsonResponse(
                {"message": "Register failed"}, safe=False, status=status.HTTP_200_OK
            )


# 用户退出登录
@api_view(["GET", "POST"])
def user_logout(request):
    if request.method == "GET":
        return JsonResponse(
            {"message": "get test"}, safe=False, status=status.HTTP_200_OK
        )
    elif request.method == "POST":
        json_str = request.body
        json_dict = json.loads(json_str)
        if User.objects.get(pk=json_dict.get("account", None)) is not None:
            sessionKey = json_dict.get("session", None)
            print(sessionKey)
            if LoginStatusManager.is_user_logged_in(sessionKey):
                LoginStatusManager.set_user_logged_out(sessionKey)
                return JsonResponse(
                    {
                        "status": 100,
                    },
                    safe=False,
                    status=status.HTTP_200_OK,
                )
            else:
                return JsonResponse(
                    {
                        "status": 101,
                    },
                    safe=False,
                    status=status.HTTP_200_OK,
                )
        else:
            return JsonResponse(
                {
                    "status": 104,
                },
                safe=False,
                status=status.HTTP_200_OK,
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
