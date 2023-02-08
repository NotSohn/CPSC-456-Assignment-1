import socket

target_host = "127.0.0.1"
target_port = 80

# create a socket object
client = socket.REPLACE_ME(socket.REPLACE_ME, socket.REPLACE_ME)

# send some data
client.sendto(b"AAABBBCCC", (REPLACE_ME, REPLACE_ME))

# receive some data
data, addr = client.REPLACE_ME(4096)

client.close()

print(data)
