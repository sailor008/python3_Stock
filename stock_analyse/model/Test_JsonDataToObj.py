class Result(object):
    def __init__(self, code, message, response=None):
        if response is None:
            response = []
        self.code = code
        self.message = message
        self.response = response


test_str = '{"code":200,"message":"发送成功","response":[{"code":2,"message":"xxxxxxxx","mobile":"xxxxxx","taskId":null},{"code":2,"message":"xxxxxx","mobile":"xxxxxx","taskId":null}]}'

jsonAttrs = json.loads(test_str)
result = Result(**jsonAttrs)
print("test log attr=> result = %s"%result.message)