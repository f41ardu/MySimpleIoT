#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://gist.github.com/tliron/8e9757180506f25e46d9


import threading
from postAPI2 import postAPI
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer



def run(server_class=HTTPServer, handler_class=postAPI, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
        print 'Stopping httpd ...'
        httpd.server_close()

def run_server(myport=8000):
    global data
    thread = threading.Thread(target = run(port=int(myport)))
    thread.start()
    return thread


if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        run_server(port=int(argv[1]))
    else:
        run_server()

   

