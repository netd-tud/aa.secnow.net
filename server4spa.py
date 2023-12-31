#!/usr/bin/env python3

# Pirated from:
# https://gist.github.com/iktakahiro/2c48962561ea724f1e9d

# Inspired by https://gist.github.com/jtangelder/e445e9a7f5e31c220be6
# Python3 http.server for Single Page Application

import urllib.parse
import http.server
import socketserver
import re
import os
from pathlib import Path

# Serve from public directory
os.chdir(os.path.join(os.getcwd(), 'public'))

HOST = ('0.0.0.0', 8000)
pattern = re.compile('.png|.jpg|.jpeg|.js|.css|.ico|.gif|.svg|.json', re.IGNORECASE)

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url_parts = urllib.parse.urlparse(self.path)
        request_file_path = Path(url_parts.path.strip("/"))

        ext = request_file_path.suffix
        if not request_file_path.is_file() and not pattern.match(ext):
            self.path = 'index.html'

        return http.server.SimpleHTTPRequestHandler.do_GET(self)


httpd = socketserver.TCPServer(HOST, Handler)
httpd.serve_forever()
