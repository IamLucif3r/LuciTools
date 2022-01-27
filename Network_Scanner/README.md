# Network Scanner 🔎

This Network Scanner Tool can  be used to:
  - Discover all Devices Connected in Network.
  - Get IP Addresses of every device.
  - Get MAC Address associated with each device.

 ## Network Scanner Algorithm 💻
 
 The tool follows the following Algorithm to find the clients connected in network:
 
```txt 
1.Create arp request directed to broadcast MAC asking for IP.
2.Send packet and receive response.
3.Parse the response.
4.Print result
```

## Usage

The tool is built using Python. This tool can be executed like a normal Python Program.

```bash

python Network_Scanner.py -t targetIP/IPrange
```
E.g: **python Network_Scanner.py -t 192.168.0.1/24**

**Note** - Run with ```'sudo'``` in case of any security priviliges error.
