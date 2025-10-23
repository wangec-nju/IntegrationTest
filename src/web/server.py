from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/v1/docs":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"code": 200}).encode("utf-8"))


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 39061), Handler).serve_forever()
