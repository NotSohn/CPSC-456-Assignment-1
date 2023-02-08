import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.REPLACE_ME, socket.REPLACE_ME)

server.bind((REPLACE_ME, REPLACE_ME))

server.listen(5)

print("[*] Listening on %s:%d" % (bind_ip, bind_port))


# this is our client handling thread
def handle_client(client_socket):
    # just print out what the client sends
    request = client_socket.REPLACE_ME(1024)

    print("[*] Received: %s" % request)

    # send back a packet
    client_socket.REPLACE_ME(b"ACK!")
    print(client_socket.getpeername())
    client_socket.close()


while True:
    client, addr = server.REPLACE_ME()

    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))

    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=REPLACE_ME, args=(client,))
    client_handler.REPLACE_ME()
