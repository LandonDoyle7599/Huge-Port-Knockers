#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <linux/tcp.h>

struct data_t {
  uint32_t ip_addr;
  uint16_t port;
};

// Creates a data
BPF_QUEUE(port_knocked, struct data_t, 1024);

int parse_packet(struct xdp_md *xdp) {

  // Grabs the ether header out of the packet
  struct ethhdr eth;
  if (bpf_xdp_load_bytes(xdp, 0, &eth, sizeof(struct ethhdr)) < 0) {
    return XDP_PASS;
  }

  // Check if the packet is an IP packet
  if (eth.h_proto != __constant_htons(ETH_P_IP)) {
    return XDP_PASS; // Not an IP packet, skip
  }

  // Load the IP header (Ethernet header is 14 bytes)
  struct iphdr ip;
  if (bpf_xdp_load_bytes(xdp, sizeof(eth), &ip, sizeof(ip)) < 0) {
    return XDP_PASS; // Skip if IP header is not available
  }

  // Ignore packets that aren't TCP
  if (ip.protocol != 6) {
    return XDP_PASS;
  }

  struct tcphdr tcp;
  if (bpf_xdp_load_bytes(xdp, sizeof(eth) + sizeof(ip), &tcp, sizeof(tcp)) <
      0) {
    return XDP_PASS; // Skip if IP header is not available
  }

  // Ignore non SYN packets
  if (tcp.syn != 1) {
    return XDP_PASS;
  }

  // Creates a data object and pushes it up to the user space application
  uint32_t ip_src = ntohl(ip.saddr);
  uint16_t dest_port = ntohs(tcp.dest);
  struct data_t data = {.ip_addr = ip_src, .port = dest_port};

  bpf_trace_printk("%d", dest_port);

  port_knocked.push(&data, sizeof(data));

  return XDP_PASS;
}
