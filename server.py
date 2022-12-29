from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

import json
import torch

camembert = torch.hub.load('pytorch/fairseq', 'camembert')

print("Server is on")

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_OPTION (self):
        self.send_header('Access-Control-Allow-Origin', '*')

    def do_GET(self):

        pattern = "."
        try:
            query = urlparse(self.path).query
            pattern = parse_qs(query)["pattern"][0]
        except Exception as e:
            pass
        response = "[]"
        try:
            pass
            response = json.dumps(list(map(lambda x: x[2].strip(), camembert.fill_mask(pattern, topk=10000))))
        except Exception:
            pass
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(f"{response}".encode('utf-8'))


httpd = HTTPServer(('0.0.0.0', 3000), SimpleHTTPRequestHandler)
httpd.serve_forever()