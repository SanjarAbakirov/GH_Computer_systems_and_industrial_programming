import socket
import threading
from datetime import datetime
import json
import urllib.parse

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
# SERVER = "192.168.31.127"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)

users_db = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "active": True},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "active": True}
]
next_user_id = 3

# web scrapping


class HTTPRequest:

    def __init__(self, raw_request):
        self.method = ""
        self.path = ""
        self.version = ""
        self.headers = {}
        self.body = ""
        self.query_params = {}
        self.parse_request(raw_request)

    def parse_request(self, raw_request):
        try:
            lines = raw_request.split('\r\n')
            if not lines:
                return

            request_line = lines[0]
            parts = request_line.split(' ')
            if len(parts) == 3:
                self.method, full_path, self.version = parts

                path_parts = full_path.split('?', 1)
                self.path = path_parts[0]
                if len(path_parts) > 1:
                    self.query_params = self.parse_query_params(path_parts[1])

            i = 1
            while i < len(lines) and lines[i]:
                if ':' in lines[i]:
                    key, value = lines[i].split(':', 1)
                    self.headers[key.strip()] = value.strip()
                i += 1

            if i + 1 < len(lines):
                self.body = '\r\n'.join(lines[i+1:])

        except Exception as e:
            print(f"Error parsing request: {e}")

    def parse_query_params(self, query_string):
        params = {}
        for param in query_string.split('&'):
            if '=' in param:
                key, value = param.split('=', 1)
                params[urllib.parse.unquote(key)] = urllib.parse.unquote(value)
        return params

    def get_json(self):
        """Parse JSON body"""
        try:
            return json.loads(self.body) if self.body else {}
        except json.JSONDecodeError:
            return {}


class HTTPResponse:

    def __init__(self, status_code=200, body="", content_type="text/plain", headers=None):
        self.status_code = status_code
        self.body = body
        self.content_type = content_type
        self.headers = headers or {}

    def build(self):
        status_codes = {
            200: "200 OK",
            201: "201 Created",
            204: "204 No Content",
            400: "400 Bad Request",
            404: "404 Not Found",
            405: "405 Method Not Allowed",
            500: "500 Internal Server Error"
        }
        status_text = status_codes.get(
            self.status_code, "500 Internal Server Error")

        response = f"HTTP/1.1 {status_text}\r\n"
        response += f"Content-Type: {self.content_type}\r\n"
        response += f"Content-Length: {len(self.body.encode('utf-8'))}\r\n"
        response += "Connection: close\r\n"
        response += f"Server: CustomPythonServer/1.0\r\n"
        response += f"Date: {datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}\r\n"

        for key, value in self.headers.items():
            response += f"{key}: {value}\r\n"

        response += "\r\n"
        response += self.body

        return response


def create_http_response(status_code=200, body="", content_type="text/plain", headers=None):
    response = HTTPResponse(status_code, body, content_type, headers)
    return response.build()


def handle_users_api(request):
    global next_user_id, users_db

    if request.method == "GET":
        if 'id' in request.query_params:
            user_id = int(request.query_params['id'])
            user = next((u for u in users_db if u['id'] == user_id), None)
            if user:
                return create_http_response(200, json.dumps({"user": user}), "application/json")
            else:
                return create_http_response(404, json.dumps({"error": "User not found"}), "application/json")
        else:

            return create_http_response(200, json.dumps({"users": users_db}), "application/json")

    elif request.method == "POST":

        try:
            data = request.get_json()
            if not data or 'name' not in data or 'email' not in data:
                return create_http_response(400, json.dumps({"error": "Name and email are required"}), "application/json")

            new_user = {
                "id": next_user_id,
                "name": data['name'],
                "email": data['email'],
                "active": True
            }
            users_db.append(new_user)
            next_user_id += 1

            return create_http_response(201, json.dumps({
                "message": "User created successfully",
                "user": new_user
            }), "application/json")
        except Exception as e:
            return create_http_response(500, json.dumps({"error": str(e)}), "application/json")

    elif request.method == "PUT":
        try:
            data = request.get_json()
            if 'id' not in data:
                return create_http_response(400, json.dumps({"error": "User ID is required"}), "application/json")

            user_id = data['id']
            user = next((u for u in users_db if u['id'] == user_id), None)

            if not user:
                return create_http_response(404, json.dumps({"error": "User not found"}), "application/json")

            if 'name' in data:
                user['name'] = data['name']
            if 'email' in data:
                user['email'] = data['email']
            if 'active' in data:
                user['active'] = data['active']

            return create_http_response(200, json.dumps({
                "message": "User updated successfully",
                "user": user
            }), "application/json")
        except Exception as e:
            return create_http_response(500, json.dumps({"error": str(e)}), "application/json")

    else:
        return create_http_response(405, json.dumps({"error": "Method not allowed"}), "application/json")


def handle_http_request(raw_request):
    try:
        request = HTTPRequest(raw_request)
        print(f"[HTTP] {request.method} {request.path}")

        # Статические маршруты
        if request.path == "/":
            html_content = """
            <html>
                <head>
                    <title>Custom HTTP Server</title>
                    <style>
                        body { font-family: Arial, sans-serif; margin: 40px; }
                        .container { max-width: 800px; margin: 0 auto; }
                        .api-link { display: block; margin: 10px 0; padding: 10px; background: #f0f0f0; }
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h1>Welcome to Custom HTTP Server</h1>
                        <p>Available endpoints:</p>
                        <a class="api-link" href="/status">Server Status</a>
                        <a class="api-link" href="/api/users">Users API</a>
                        <a class="api-link" href="/api/info">Server Info</a>
                    </div>
                </body>
            </html>
            """
            return create_http_response(200, html_content, "text/html")

        elif request.path == "/status":
            status_info = {
                "server": SERVER,
                "time": datetime.now().isoformat(),
                "active_connections": threading.active_count() - 1,
                "total_users": len(users_db)
            }
            html = f"""
            <html>
                <body>
                    <h1>Server Status</h1>
                    <pre>{json.dumps(status_info, indent=2)}</pre>
                    <a href="/">Back to Home</a>
                </body>
            </html>
            """
            return create_http_response(200, html, "text/html")

        elif request.path == "/api/info":
            info = {
                "name": "Custom HTTP Server",
                "version": "1.0",
                "protocol": "HTTP/1.1",
                "endpoints": [
                    "GET /api/users",
                    "POST /api/users",
                    "PUT /api/users",
                    "GET /status",
                    "GET /api/info"
                ]
            }
            return create_http_response(200, json.dumps(info), "application/json")

        elif request.path.startswith("/api/users"):
            return handle_users_api(request)

        else:
            error_html = """
            <html>
                <body>
                    <h1>404 - Page Not Found</h1>
                    <p>The requested URL was not found on this server.</p>
                    <a href="/">Go to Homepage</a>
                </body>
            </html>
            """
            return create_http_response(404, error_html, "text/html")

    except Exception as e:
        print(f"[ERROR] Handling request: {e}")
        return create_http_response(500, f"Internal Server Error: {e}")


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    try:
        request_data = ""
        conn.settimeout(5.0)  # Таймаут 5 секунд

        while True:
            chunk = conn.recv(4096).decode(FORMAT)
            request_data += chunk

            if '\r\n\r\n' in request_data:
                if 'Content-Length:' in request_data:
                    headers_part = request_data.split('\r\n\r\n')[0]
                    content_length = 0
                    for line in headers_part.split('\r\n'):
                        if line.lower().startswith('content-length:'):
                            content_length = int(line.split(':')[1].strip())
                            break

                    body_part = request_data.split(
                        '\r\n\r\n')[1] if '\r\n\r\n' in request_data else ""
                    while len(body_part) < content_length:
                        chunk = conn.recv(4096).decode(FORMAT)
                        body_part += chunk

                    request_data = headers_part + '\r\n\r\n' + body_part
                break

        if request_data.strip():
            http_response = handle_http_request(request_data)
            conn.send(http_response.encode(FORMAT))

    except socket.timeout:
        print(f"[TIMEOUT] {addr} - connection timeout")
    except Exception as e:
        print(f"[ERROR] with {addr}: {e}")
        error_response = create_http_response(500, "Internal Server Error")
        conn.send(error_response.encode(FORMAT))
    finally:
        conn.close()
        print(f"[DISCONNECTED] {addr}")


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    print(f"[ACCESS] Open http://{SERVER}:{PORT} in your browser")

    while True:
        try:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.daemon = True
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        except KeyboardInterrupt:
            print("\n[SHUTDOWN] Server is shutting down...")
            break
        except Exception as e:
            print(f"[ERROR] Accepting connection: {e}")


if __name__ == "__main__":
    print("[STARTING] HTTP server is starting...")
    start()
