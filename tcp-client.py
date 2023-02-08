import socket

target_host = "www.google.com"
target_port = 80

# create a socket object
client = socket.REPLACE_ME(socket.REPLACE_ME, socket.REPLACE_ME)

# connect the client
client.connect((REPLACE_ME, REPLACE_ME))

# send some data
client.REPLACE_ME(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive data
response = client.recv(4096)

client.close()

print(response)
