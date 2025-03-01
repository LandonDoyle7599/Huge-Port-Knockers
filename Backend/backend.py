#!/usr/bin/python3

import threading
import time
from api import API
from port_knock_track import PortKnock
from helloTcpServer import HelloTcpServer
from hello_world import ebpf

class Backend:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}
        self.api = API(self.data, self.lock)
        self.port_knock = PortKnock(self.data, self.lock)
        self.stop_event = threading.Event()
        self.helloServer = HelloTcpServer(self.port_knock, self.stop_event)

        # Start port-knock thread for processing knock attempts
    
        self.thread_two = threading.Thread(target=self.port_knock_run, daemon=True)
        self.thread_two.start()
        self.thread_server = threading.Thread(target=self.helloServer.runServer, daemon=True)
        self.thread_server.start()

    def port_knock_run(self):
        while not self.stop_event.is_set():
            #time.sleep(2)
            #self.port_knock.knock_attempt('10.10.10.10', 5206)
            #time.sleep(2)
            #self.port_knock.print_map()
            #self.port_knock.knock_attempt('10.10.10.10', 20)
            #time.sleep(2)
            #self.port_knock.print_map()
            #self.port_knock.knock_attempt('10.10.10.10', 5206)
            #time.sleep(2)
            #self.port_knock.print_map()
            #self.port_knock.knock_attempt('10.10.10.10', 48149)
            #time.sleep(2)
            #self.port_knock.knock_attempt('10.10.10.10', 20367)
            #time.sleep(2)
            #self.port_knock.print_map()
            #self.port_knock.knock_attempt('10.10.10.10', 9580)
            #time.sleep(2)
            #self.port_knock.print_map()
            ebpf(self.port_knock)
            #while True:
            #    with self.lock:
            #        self.port_knock.print_map()
            #    time.sleep(5)

    def shutdown(self):
        self.stop_event.set()
        sys.exit(0)
    
if __name__ == '__main__':
    backend = Backend()
    # Now the API will run in the main thread
    backend.api.run()
