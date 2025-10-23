import pytest
import os, json, requests, subprocess
from enum import Enum


class IntegrationTest:
    def __init__(self):
        self.protocol = Protocol.HTTP
        self.host: str = "localhost"
        self.port: int = 39061
        self.headers: dict | None = None
        self.root_path: str = os.path.abspath("..")
        self.cases_dir: str = os.path.join(self.root_path, "resources")
        self.web_service: str = os.path.join(self.root_path, "src", "web", "server.py")

    def test_get_docs(self):
        self.test("/api/v1/docs", "cases.json")

    @pytest.fixture(scope="class")
    def start_server(self):
        subprocess.Popen(["python", self.web_service])

    def test(self, path: str, case_file_name: str):
        cases: list = self.decode_case_file(
            os.path.join(self.cases_dir, case_file_name)
        )
        for case in cases:
            assert self.encode_json(case["response"]) == self.request(
                case["method"],
                self.get_url(path),
                request_body=self.encode_json(case["request"]),
            )

    def decode_case_file(self, case_file_path: str):
        with open(case_file_path, "r") as f:
            return json.load(f)

    def request(self, method: str, url: str, *, request_body: str):
        if method == "get":
            return requests.get(url, headers=self.headers, data=request_body)
        elif method == "post":
            return requests.post(url, headers=self.headers, data=request_body)
        elif method == "put":
            return requests.put(url, headers=self.headers, data=request_body)
        elif method == "delete":
            return requests.delete(url, headers=self.headers, data=request_body)
        else:
            raise URLNotFoundError

    def encode_json(self, string):
        if string == "" or string is None:
            return None
        else:
            return json.loads(string)

    def get_url(self, path: str):
        return os.path.join(f"{self.protocol.value}://{self.host}:{self.port}", path)


class Protocol(Enum):
    HTTP = "http"
    HTTPS = "https"


class URLNotFoundError(Exception):
    pass
