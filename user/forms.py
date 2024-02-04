from django import forms
from common.models import User


class RegistrationForm(forms.Form):
    class Meta:
        model = User
        fields = [
            "user_phone",
            "user_email",
            "user_account_type",
            "user_wx_info",
            "user_password",
            "user_name",
            "user_real_info",
            "user_real_status",
            "user_privilege",
            "user_extend",
        ]
