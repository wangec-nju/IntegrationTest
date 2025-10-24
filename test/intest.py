import pytest
import os, json, time, requests, subprocess
from enum import Enum

# 这个文件专门存放接口测试类。
# 一般来讲，大家只需要配置Configuration的变量，写好样例JSON，调用test()测试就行。
# 关于怎么写样例JSON，请看根目录下的README.md


class Protocol(Enum):
    HTTP = "http"
    HTTPS = "https"


class URLNotFoundError(Exception):
    pass


# Configuration
protocol = Protocol.HTTP  # 服务器选用的协议，可以选择HTTP和HTTPS
host: str = "localhost"  # 服务器的主机名或IP地址
port: int = 39061  # 服务器开放RESTful API的端口
# 请求的时候需要附加的HEADERS
headers: dict | None = None
# 工作区根目录的绝对路径，一般指src/、test/等文件夹的父目录
root_path: str = os.path.abspath(".")
# 样例JSON文件存放目录的绝对路径
cases_dir: str = os.path.join(root_path, "resources")
# 服务器文件的绝对路径
web_service: str = os.path.join(root_path, "src", "web", "server.py")


class IntegrationTest:
    @classmethod
    def setup_class(self):
        # 在运行整个测试类之前只运行一次的函数，一般用来启用服务器
        subprocess.Popen(["python", web_service])
        time.sleep(5)  # 不能省，保证服务器运转正常再开始访问

    def test_get_docs(self):
        # 这个函数是用来测试接口的，会在运行pytest的时候运行
        self.test("/api/v1/docs", "cases.json")

    def test(self, path: str, case_file_name: str):
        # 这个函数是对具体测试过程的封装，一般不需要修改，pytest运行的时候也不会运行这个函数
        cases: list = self.decode_case_file(os.path.join(cases_dir, case_file_name))
        for case in cases:
            assert (
                case["response"]
                == self.request(
                    case["method"],
                    self.get_url(path),
                    request_body=self.decode_json(case["request"]),
                ).json()
            )

    def decode_case_file(self, case_file_path: str):
        # 这个函数是用来解析样例JSON文件的
        with open(case_file_path, "r") as f:
            return json.load(f)

    def request(self, method: str, url: str, *, request_body: str):
        # 这个函数是对具体请求过程的封装
        if method == "get":
            return requests.get(url, headers=headers, data=request_body)
        elif method == "post":
            return requests.post(url, headers=headers, data=request_body)
        elif method == "put":
            return requests.put(url, headers=headers, data=request_body)
        elif method == "delete":
            return requests.delete(url, headers=headers, data=request_body)
        else:
            raise URLNotFoundError

    def decode_json(self, obj):
        # 这个函数是为了保证解析JSON的时候获取到None就返回None
        if obj is None:
            return None
        else:
            return json.dumps(obj)

    def get_url(self, path: str):
        # 这个是为了标准化生成需要访问的URL
        if path[0] != "/":
            path = "/" + path
        return f"{protocol.value}://{host}:{port}" + path
