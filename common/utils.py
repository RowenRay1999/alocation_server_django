import random
import bcrypt
from django.db import transaction
from common.models import User


def assign_user_id(instance: User):
    if instance.user_account is None:
        # 事务确保原子性操作
        with transaction.atomic():
            while True:
                # 生成随机的用户ID
                user_count = User.objects.count()
                if user_count < 89999:
                    user_id = random.randint(10001, 99999)
                elif user_count <= 899999:
                    user_id = random.randint(100000, 999999)
                elif user_count <= 8999999:
                    user_id = random.randint(1000000, 9999999)
                else:
                    user_id = random.randint(10000000, 1e12 - 1)

                # 检查用户ID是否唯一
                if not User.objects.filter(user_account=user_id).exists():
                    instance.user_account = user_id
                    break


def gen_password(raw_password):
    return bcrypt.hashpw(raw_password.encode("utf-8"), bcrypt.gensalt())


def check_password(raw_password, ciphertext):
    return bcrypt.checkpw(raw_password.encode("utf-8"), ciphertext.encode("utf-8"))
