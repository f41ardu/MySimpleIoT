
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#import SocketServer

data = [0] * 50
counter = 0

class postAPI(BaseHTTPRequestHandler):
    #counter = 0
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
                
    def do_POST(self):
        global counter,data
        # Doesn't do anything with posted data
        self.send_response(200)
#        print(self.headers['Content-Type'])
#        print(self.headers['X-THINGSPEAKAPIKEY'])
#        print(self.headers['Content-Length'])
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        if counter > 49:
            counter = 0
        data[counter] = post_data
        counter=counter+1
        
        print counter, data
        #print(len(post_data),post_data)
        #print(post_data.split('&'))
             
    
