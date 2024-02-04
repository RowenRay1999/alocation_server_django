from datetime import datetime
import json
from django_redis import get_redis_connection


class LoginStatusManager:
    @staticmethod
    def set_user_logged_in(user_id):
        connection = get_redis_connection("default")
        key = f"user:{user_id}:logged_in:{int(datetime.now().timestamp())}"
        connection.set(key, json.dumps(True))
        connection.expire(key, 60 * 60 * 24 * 30)
        # 设置过期时间为30天，过期前需要客户端自动重新申请
        return key

    @staticmethod
    def is_user_logged_in(key):
        connection = get_redis_connection("default")
        return connection.get(key) == b"true"
    
    @staticmethod
    def set_user_logged_out(key):
        connection = get_redis_connection("default")
        return connection.delete(key)
