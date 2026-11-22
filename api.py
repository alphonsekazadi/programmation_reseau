from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class monAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/devices":
            corps = json.dumps({"nom": "Routeur", "IP": "192.168.1.1"})
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(corps.encode())
        else:
            self.send_response(404)
            self.end_headers()
HTTPServer(("127.0.0.1", 8000), monAPI).serve_forever()
            