import time
import os
from http.server import HTTPServer, BaseHTTPRequestHandler


DEFAULT_PORT: int = 8080


class Server(BaseHTTPRequestHandler):
    @property
    def hostname(self) -> str | None:
        return os.getenv("HOSTNAME", None)

    def do_GET(self) -> None:
        response = f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>
            TestApp
        </title>
    </head>
    <body>
    <p>
    Hi from server at {time.asctime() + (' !' if self.hostname is None else ' from ' + self.hostname + ' !')}
    <br></br>
    Counter: 1
    <p>
    </body>
</html>"""
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(response, 'utf-8'))


def main() -> None:
    print("will construct server")
    port: int = int(os.getenv("SERVER_HTTP_PORT", DEFAULT_PORT))
    httpd = HTTPServer(('0.0.0.0', port), Server)
    print("constructed server")

    print("will server forever...\nCtrl + C to exit\n")
    httpd.serve_forever()


if __name__ == '__main__':
    main()
