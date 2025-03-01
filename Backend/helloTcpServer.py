import socket
from port_knock_track import PortKnock


class HelloTcpServer():
    def __init__(self, port_knock_track):
        self.port_knock_track = port_krock_track
        self.tcpListenSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverAddr = (0.0.0.0, 8080)
        self.tcpListenSock.bind(self.serverAddr)
            
    def runServer
        self.tcpListenSock.listen(1)
        while True:
            connection, clientAddr = self.tcpListenSock.accept()
            # check if this client address is allowed
            # TODO use mutex
            if self.port_knock_track.checkIpAllowed(clientAddr)
                # OK!
                connection.write("Hello")
                connection.close()
            else
                # How about NO
                connection.close()

