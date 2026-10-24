from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")

    def do_POST(self):
        if self.path == "/webhook":
            length = int(self.headers.get('Content-Length', 0))
            data = self.rfile.read(length)

            print("\n===== ALERT RECEIVED =====")
            print(data.decode())

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"status":"received"}')

server = HTTPServer(("0.0.0.0", 5000), Handler)

print("Sherlock started on port 5000")

server.serve_forever()
