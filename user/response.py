import json


class errMsg:
    def __init__(self, errorCode, errorInfo):
        self.errorCode = errorCode
        self.errorInfo = errorInfo

    def to_json(self):
        return json.dumps(self.__dict__)
