import socket
from port_knock_track import PortKnock
import time


class HelloTcpServer():
    def __init__(self, port_knock_track, stop_event):
        self.port_knock_track = port_knock_track
        self.stop_event = stop_event
        option = 1
        self.tcpListenSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpListenSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcpListenSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)  # Add this line
        self.serverAddr = ('0.0.0.0', 8080)
        self.tcpListenSock.bind(self.serverAddr)
            
    def runServer(self):
        while not self.stop_event.is_set():
            self.tcpListenSock.listen(1)
            while True:
                connection, clientAddr = self.tcpListenSock.accept()
                # check if this client address is allowed
                # TODO use mutex
                print("here!!!!")
                if self.port_knock_track.checkIpAllowed(clientAddr):
                    print("I belong here!!!!")
                    time.sleep(2)
                    self.port_knock_track.connection_established(clientAddr)
                    # OK!
                    data = str.encode("Hello")
                    connection.sendall(data)
                    connection.shutdown(self.tcpListenSock.SHUT_RDWR)
                    connection.close()
                    time.sleep(2)
                    self.port_knock_track.remove_ip(clientAddr)
                else:
                    # How about NO
                    connection.shutdown(self.tcpListenSock.SHUT_RDWR)
                    connection.close()

