from flask import Flask, render_template
import os, platform, psutil, socket
from decimal import *


class System:
    def __init__(self):
        # Operating system
        self.osSystem = platform.system()
        self.osRelease = platform.release()
        # CPU
        self.cpuUsage = psutil.cpu_percent(interval = 1)
        # Virtual memory
        memory = psutil.virtual_memory()
        self.memoryFree = memory.percent
        self.memoryTotal = f"{memory.total / (1024**3):.2f}"
        self.memoryUsed = f"{memory.used / (1024**3):.2f}"
        # Socket
        self.socketHostname = socket.gethostname()
        self.socketIp = socket.gethostbyname(self.socketHostname)

        self.render_array()
    
    def render_array(self):

        return {
            "os": {
                "system": self.osSystem,
                "release": self.osRelease
            },
            "cpu": {
                "used": self.cpuUsage
            },
            "memory": {
                "free": self.memoryFree,
                "total": self.memoryTotal,
                "used": self.memoryUsed,
            },
            "socket": {
                "hostname": self.socketHostname,
                "ip": self.socketIp
            }
        }

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", system = System().render_array())