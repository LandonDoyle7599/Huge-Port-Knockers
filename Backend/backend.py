import threading
import time
from api import API
from port_knock_track import PortKnock

class Backend:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}
        self.api = API(self.data, self.lock)
        self.port_knock = PortKnock(self.data, self.lock)

        # Start port-knock thread for processing knock attempts
        self.thread_two = threading.Thread(target=self.port_knock_run)
        self.thread_two.start()

    def port_knock_run(self):
        while True:
            with self.lock:
                self.port_knock.print_map()
            time.sleep(5)

    
if __name__ == '__main__':
    backend = Backend()
    # Now the API will run in the main thread
    backend.api.run()
