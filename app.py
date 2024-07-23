from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8082


class MyServer(BaseHTTPRequestHandler):
    '''Класс отвечает за обработку входящих запросов'''

    filename = 'index.html'

    def __get_index(self):

        with open(self.filename, 'r') as file:
            response = file.read()

        return response

    def do_GET(self):
        '''Метод для обработки входящих GET запросов'''

        query_components = parse_qs(urlparse(self.path).query)
        page_address = query_components.get('page')
        page_content = self.__get_index()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
