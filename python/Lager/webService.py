#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://gist.github.com/tliron/8e9757180506f25e46d9

from BaseHTTPServer import HTTPServer
from postAPI2 import postAPI

def run(server_class=HTTPServer, handler_class=postAPI, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    print 'Stopping HTTP server'
    httpd.server_close()


if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
