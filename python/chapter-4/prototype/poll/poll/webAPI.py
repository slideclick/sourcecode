import SimpleHTTPServer
import SocketServer
import os


print "serving at port 8001"
SocketServer.TCPServer(("", 8002),
                       SimpleHTTPServer.SimpleHTTPRequestHandler).serve_forever()