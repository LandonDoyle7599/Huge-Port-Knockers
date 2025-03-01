#!/usr/bin/python3

from time import sleep
from bcc import BPF
from bcc.utils import printb


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
        (task, pid, cpu, flags, ts, msg) = bpf.trace_fields()
        print(queue.pop())
    except KeyError as e:
        print(f"Queue is empty")
    except KeyboardInterrupt:
        exit()
    printb(b"%-18.9f %-16s %-6d %s" % (ts, task, pid, msg))
    sleep(0.5)
