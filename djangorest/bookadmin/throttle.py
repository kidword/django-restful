import time
from rest_framework.throttling import SimpleRateThrottle

"""

VISIT_RECORD = {}


class VisitThrottle(BaseThrottle):
    def __init__(self):
        self.history = None

    def allow_request(self, request, view):
        remote_addr = self.get_ident(request)

        ctime = time.time()
        if remote_addr not in VISIT_RECORD:
            VISIT_RECORD[remote_addr] = [ctime, ]
            return True

        history = VISIT_RECORD.get(remote_addr)
        self.history = history

        while history and history[-1] < ctime - 60:
            history.pop()

        if len(history) < 3:
            history.insert(0, ctime)
            return True

    def wait(self):
        ctime = time.time()

        return 60 - (ctime - self.history[-1])

"""


# 匿名用户频率限制
class VisitThrottle(SimpleRateThrottle):
    scope = 'speed'

    def get_cache_key(self, request, view):
        return self.get_ident(request)


# 登录用户频率限制
class UserThrottle(SimpleRateThrottle):
    scope = 'userspeed'  # 速度范围

    def get_cache_key(self, request, view):
        """唯一标识"""
        return request.user.username
