import socket

target_host = "127.0.0.1"
target_port = 80

# 1.create a Socket Object
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 2. Send Some Data using sendto
client.sendto("AAABBBCCC",(target_host,target_port))

# 3. Receive Some Data
data, addr = client.recvfrom(4096)

print data