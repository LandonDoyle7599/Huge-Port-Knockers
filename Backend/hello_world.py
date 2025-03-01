#!/usr/bin/python3

from time import sleep
from bcc import BPF
import socket, struct

def ebpf(port_knock_tracker):
    tracker = port_knock_tracker
    # Loads the c file into the BPF program
    bpf = BPF(src_file="network.c")
    
    # Interface to monitor with BPF
    interface = "enp0s3"
    
    # Attaches xdp function to xdp call in the kernel
    fn = bpf.load_func("parse_packet", BPF.XDP)
    BPF.attach_xdp(interface, fn, 0)
    
    print("BPF program has been loaded...")
    
    # Grabs the map associated with the BPF program
    queue = bpf["port_knocked"]
    
    # Reads results from BPF programs (User Space)
    while True:
        try:
            data = queue.pop()
            ipv4 = socket.inet_ntoa(struct.pack('!L', data.ip_addr))
            tracker.knock_attempt(ipv4, data.port)
            print("IP: {}, PORT: {}".format(ipv4, data.port))
        except KeyError as e:
            sleep(0.5)
            continue
        except KeyboardInterrupt:
            exit()
        sleep(0.5)
           
