import hmac
import hashlib

class PortKnock():
    def __init__(self, knock_map, lock):
        self.knock_map = knock_map
        self.lock = lock
        self.hash_secrets = ['huge','port','knockers','secured','leggo']

    def knock_attempt(self, src_ip, dst_port):
        if src_ip not in self.knock_map:
            self.create_port_sequence(src_ip)
        port_tuples, _ = self.knock_map.get(src_ip)

        updated_tuples = []
        successful_attempt = False
        knock_index = 0
        #loop through to see where we are at in the sequence
        for req_port, knocked in port_tuples:
            knock_index += 1
            if successful_attempt:
                #finish updating the udpated tuples
                updated_tuples.append((req_port, False))
            elif knocked:
                updated_tuples.append((req_port, True))
            else:
                if(dst_port == req_port):
                    updated_tuples.append((req_port, True))
                    successful_attempt = True
                    if(knock_index == len(port_tuples)-1):
                        port_to_open, _ = port_tuples[-1]
                        self.open_connection_port(src_ip, port_to_open)
                else:
                    #incorrect sequence, reset
                    updated_tuples = []
                    for req_port, knocked in port_tuples:
                        updated_tuples.append((req_port, False))
                    break
        with self.lock:
            self.knock_map[src_ip] = (updated_tuples, not successful_attempt)

    def print_map(self):
        print(self.knock_map)


    def create_port_sequence(self, src_ip):
        port_tups = []
        ports = self.generate_ports(src_ip)

        for port_num in ports:
            port_tups.append((port_num, False))

        with self.lock:
            self.knock_map[src_ip] = (port_tups, True)


    def generate_ports(self, src_ip):
        ports = []
        for hash_secret in self.hash_secrets:
            hmac_object = hmac.new(hash_secret.encode(), src_ip.encode(), hashlib.sha256)
            ports.append(int(hmac_object.hexdigest(), 16) % 65535)
        return ports


    def open_connection_port(self, ip, port):
        print(f"opening port {port} for {ip}")


    def get_knock_map(self):
        return self.knock_map

    def checkIpAllowed(self, ip):
        if src_ip not in self.knock_map:
            return False;
        port_tuples, _ = self.knock_map.get(ip)
        knock_index = 0
        #loop through to see where we are at in the sequence
        for req_port, knocked in port_tuples:
            knock_index += 1
            if knocked == False:
                return False;
        # at this point, all ports have been knocked,
        # fully authenticated
        return True
