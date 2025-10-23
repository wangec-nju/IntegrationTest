import pytest
import os, json, requests, subprocess
from enum import Enum


class Protocol(Enum):
    HTTP = "http"
    HTTPS = "https"


class URLNotFoundError(Exception):
    pass


protocol = Protocol.HTTP
host: str = "localhost"
port: int = 39061
headers: dict | None = None
root_path: str = os.path.abspath(".")
cases_dir: str = os.path.join(root_path, "resources")
web_service: str = os.path.join(root_path, "src", "web", "server.py")


class IntegrationTest:
    @classmethod
    def setup_class(self):
        subprocess.Popen(["python", web_service])

    def test_get_docs(self):
        self.test("/api/v1/docs", "cases.json")

    def test(self, path: str, case_file_name: str):
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
        with open(case_file_path, "r") as f:
            return json.load(f)

    def request(self, method: str, url: str, *, request_body: str):
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
        if obj is None:
            return None
        else:
            return json.dumps(obj)

    def get_url(self, path: str):
        return f"{protocol.value}://{host}:{port}" + path
