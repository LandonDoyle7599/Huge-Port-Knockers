import threading
import time
from api import API
from port_knock_track import PortKnock
# from HelloTcpServer import HelloTcpServer

class Backend:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}
        self.api = API(self.data, self.lock)
        self.port_knock = PortKnock(self.data, self.lock)
        # self.helloServer = HelloTcpServer()

        # Start port-knock thread for processing knock attempts
    
        self.thread_two = threading.Thread(target=self.port_knock_run)
        self.thread_two.start()
        # self.thread_server = threading.Thread(target=self.helloServer.runServer)
        # self.thread_server.start()

    def port_knock_run(self):
        time.sleep(2)
        self.port_knock.knock_attempt('10.10.10.10', 5206)
        time.sleep(2)
        self.port_knock.print_map()
        self.port_knock.knock_attempt('10.10.10.10', 20)
        time.sleep(2)
        self.port_knock.print_map()
        self.port_knock.knock_attempt('10.10.10.10', 5206)
        time.sleep(2)
        self.port_knock.print_map()
        self.port_knock.knock_attempt('10.10.10.10', 48149)
        time.sleep(2)
        self.port_knock.knock_attempt('10.10.10.10', 20367)
        time.sleep(2)
        self.port_knock.print_map()
        self.port_knock.knock_attempt('10.10.10.10', 9580)
        time.sleep(2)
        self.port_knock.print_map()
        while True:
            with self.lock:
                self.port_knock.print_map()
            time.sleep(5)
    
if __name__ == '__main__':
    backend = Backend()
    # Now the API will run in the main thread
    backend.api.run()
