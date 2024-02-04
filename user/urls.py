from django.urls import path
from django.urls import re_path

from . import views

app_name = "user"

urlpatterns = [
    re_path(
        r"^login/client$",
        views.user_login,
        name="login",
    ),
    re_path(r"^register/client$", views.user_register, name="register"),
    re_path(r"^logout/client$", views.user_logout, name="logout"),
    re_path(r"^update/client/$", views.user_update_client, name="user_update_client"),
    re_path(r"^user_data/client/$", views.user_data_client, name="user_data_client"),
    re_path(
        r"^user_data/update/client/$",
        views.user_data_update_client,
        name="user_data_update_client",
    ),
    re_path(
        r"^user_base/client/$",
        views.user_base_client,
        name="user_base_client",
    ),
    re_path(
        r"^forget/pwd/client/$",
        views.user_forget_pwd_client,
        name="/forget/pwd/client",
    ),
]
