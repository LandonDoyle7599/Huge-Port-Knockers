import hmac
import hashlib
import threading


class PortKnock():
    def __init__(self, knock_map, lock):
        self.knock_map = knock_map
        self.lock = lock
        self.hash_secrets = ['huge','port','knockers','secured']

    def knock_attempt(self, src_ip, dst_port):
        if src_ip not in self.knock_map:
            self.create_port_sequence(src_ip)
        port_tuples, _, _ = self.knock_map.get(src_ip)

        updated_tuples = []
        successful_attempt = False
        knock_index = 0
        good_knock_count = 0
        #loop through to see where we are at in the sequence
        for req_port, knocked in port_tuples:
            if req_port == 8080:
                print("I promise I return this knocker")
                return
            knock_index += 1
            if successful_attempt:
                #finish updating the udpated tuples
                updated_tuples.append((req_port, False))
            elif good_knock_count == 4:
                updated_tuples = []
                for req_port, knocked in port_tuples:
                    updated_tuples.append((req_port, False))
                break
            elif knocked:
                updated_tuples.append((req_port, True))
                good_knock_count += 1
            else:
                if(dst_port == req_port):
                    updated_tuples.append((req_port, True))
                    successful_attempt = True
                else:
                    #incorrect sequence, reset
                    updated_tuples = []
                    for req_port, knocked in port_tuples:
                        updated_tuples.append((req_port, False))
                    break

        with self.lock:
            print("updating map")
            self.knock_map[src_ip] = (updated_tuples, not successful_attempt, False)

    def print_map(self):
        print(self.knock_map)


    def create_port_sequence(self, src_ip):
        port_tups = []
        ports = self.generate_ports(src_ip)

        for port_num in ports:
            port_tups.append((port_num, False))

        with self.lock:
            self.knock_map[src_ip] = (port_tups, True, False)


    def generate_ports(self, src_ip):
        ports = []
        for hash_secret in self.hash_secrets:
            hmac_object = hmac.new(hash_secret.encode(), src_ip.encode(), hashlib.sha256)
            ports.append((int(hmac_object.hexdigest(), 16) % (65535-4000)) + 4000)
        return ports


    def get_knock_map(self):
        return self.knock_map

    def checkIpAllowed(self, ip):
        if ip not in self.knock_map:
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

    def connection_established(self, ip):
        if ip not in self.knock_map:
            return
        port_tuples, failed, _  = self.knock_map.get(ip)
        print("connection")
        with self.lock:
            print("updating map")
            self.knock_map[ip] = (port_tuples, failed, True)


    def remove_ip(self, ip):
        if ip not in self.knock_map:
            return
        del self.knock_map[ip]
  

#if __name__ == '__main__':
    #{'10.10.10.10': ([(5206, False), (48149, False), (20367, False), (9580, False)], False)}
    #Pn = PortKnock({},threading.Lock() )
    #Pn.knock_attempt('10.10.10.10', 5206)
    #Pn.print_map()
    #Pn.knock_attempt('10.10.10.10', 20)
    #Pn.print_map()
    #Pn.knock_attempt('10.10.10.10', 5206)
    #Pn.print_map()
    #Pn.knock_attempt('10.10.10.10', 48149)
    #Pn.knock_attempt('10.10.10.10', 20367)
    #Pn.print_map()
    #Pn.knock_attempt('10.10.10.10', 9580)
    #Pn.print_map()
    #print(Pn.checkIpAllowed('10.10.10.10'))
