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
        self.tcpListenSock.setsockopt(socket.SO_LINGER, struct.pack('ii', l_onoff, l_linger))
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
                    data = str.encode("Knock knock.\nWho’s there?\nA broken doorbell.\nA broken doorbell who?\n...\n(You stay silent.)\n\nFriend: Uh… hello?\nYou: ...\nFriend: Are you still there?\nYou: ...\nFriend: (Getting frustrated) Fine. *A BROKEN DOORBELL, WHO?!*\nYou: Oh! Sorry, I was just demonstrating what a broken doorbell does. Anyway—knock knock.\nFriend: (Sighs) Who’s there?\nYou: Cow says.\nFriend: Cow says who?\nYou: No, cow says “moo.” But—knock knock.\nFriend: (Groaning) Who’s there?\nYou: Control freak—okay, now YOU say “control freak who?”\nFriend: Control fr—\nYou: TOO SLOW! But—knock knock.\nFriend: (Resigned) Who’s there?\nYou: Déjà vu.\nFriend: Déjà vu who?\nYou: Knock knock.\nFriend: Who’s there?\nYou: Déjà vu.\nFriend: DEJA VU WHO?!\nYou: Knock knock.\nFriend: Who’s there?\nYou: A little old lady.\nFriend: A little old lady who?\nYou: Wow, I didn’t know you could yodel!\nFriend: … I hate you.\nYou: Knock knock.\nFriend: NO.")
                    connection.sendall(data)
                    connection.shutdown(socket.SHUT_RDWR)
                    connection.close()
                    time.sleep(2)
                    self.port_knock_track.remove_ip(clientAddr)
                else:
                    # How about NO
                    connection.shutdown(socket.SHUT_RDWR)
                    connection.close()

