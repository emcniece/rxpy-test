#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json
import time

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)

        try:
          sleep_time = parsed_path.query.split('=')[1]
          print('Sleeping: ', sleep_time)
          time.sleep(int(sleep_time))
        except:
          print("Error parsing delay")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({
            'method': self.command,
            'path': self.path,
            'real_path': parsed_path.query,
            'query': parsed_path.query,
            'request_version': self.request_version,
            'protocol_version': self.protocol_version
        }).encode())
        return

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), RequestHandler)
    print('Starting server at http://localhost:8080')
    server.serve_forever()