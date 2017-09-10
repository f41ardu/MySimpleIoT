
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#import SocketServer
import ast
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

ydata = [0] * 50
ydata1 = [0] * 50

plt.ion() # set plot to animated

# make plot
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax1.set_xlabel('#')
ax1.set_title('Feinstaub')
ax1.xaxis.set_major_locator(ticker.MaxNLocator(5))
ax1.xaxis.set_minor_locator(ticker.MaxNLocator(10))
ax1.yaxis.set_major_locator(ticker.MaxNLocator(5))
ax1.yaxis.set_minor_locator(ticker.MaxNLocator(10))
line, = plt.plot(ydata, color ='r')
plt.legend([line], ['$\mu$g/m^3'])
plt.grid(True)

ax2 = fig.add_subplot(2, 2, 2)
ax2.set_xlabel('#')
ax2.set_title('Sensorspannung')
ax2.xaxis.set_major_locator(ticker.MaxNLocator(5))
ax2.xaxis.set_minor_locator(ticker.MaxNLocator(10))
ax2.yaxis.set_major_locator(ticker.MaxNLocator(5))
ax2.yaxis.set_minor_locator(ticker.MaxNLocator(10))
line1, = plt.plot(ydata1, color = 'g')
plt.legend([line1], ['Volt'])
plt.grid(True)

tdata = [0] * 50
counter = 0

def plotdata(dust,voltage):
    data=dust
    data1=voltage
    ymin = 0. #float(min(ydata))#-10
    ymax = float(max(ydata))+20
    ax1.set_ylim(ymin, ymax)
    ydata.append(data)
    ymax = float(max(ydata1))+2
    ax2.set_ylim(ymin, ymax)
    ydata1.append(data1)
    del ydata[0]
    del ydata1[0]
    line.set_xdata(np.arange(len(ydata)))
    line.set_ydata(ydata)  # update the data
    line1.set_ydata(ydata1)  # update the data1
    plt.draw() # update the plot

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
        global counter,tdata
        
        # Doesn't do anything with posted data
        self.send_response(200)
#        print(self.headers['Content-Type'])
#        print(self.headers['X-THINGSPEAKAPIKEY'])
#        print(self.headers['Content-Length'])
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        if counter > 49:
            counter = 0
        tdata[counter] = post_data
        fdata = post_data.split('&')
        field1 = fdata[1].split('=')
        field2 = fdata[2].split('=')
        dust= ast.literal_eval(field1[1])
        volt= ast.literal_eval(field2[1])
        plotdata(counter,volt)
        print counter
        counter=counter+1
        
        
        print dust,volt
        #print(len(post_data),post_data)
        #print(post_data.split('&'))
             
    
