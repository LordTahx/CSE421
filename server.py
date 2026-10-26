import socket
import threading
port = 5000
format = "utf-8"
buffer = 16
disconnected = "End"

hostname = socket.gethostname()
host_ip_address = socket.gethostbyname(hostname)

print(hostname)
print(host_ip_address)

server_socket_address = (host_ip_address, port)
print(server_socket_address)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPv4, AF_INET6 = IPv6, SOCK_STREAM = TCP
print(server)
server.bind(server_socket_address)
print(server)

server.listen()
print("Server is listening")

#while True:
    #conn, addr = server.accept()
def helper(conn, addr):
    print("Connected to", addr)
    connected = True

    while connected:
        message_length = conn.recv(buffer).decode(format)
        print("Length of the message is", message_length)

        if message_length:
            message_length = int(message_length)
            msg = conn.recv(message_length).decode(format)
            if msg == disconnected:
                conn.send("Goodbye. It was nice to serve you.".encode(format))
                print("Terminating connection with", addr)
                connected = False
            else:
                print(msg)
                conn.send("I have received your message".encode(format))
                vowels = "aeiouAEIOU"
                total = 0
                for i in msg:
                    if i in vowels:
                        total += 1
                if total == 0:
                    conn.send("Not enough vowels".encode(format))
                elif total <= 2:
                    conn.send("Enough".encode(format))
                else:
                    conn.send("Too many".encode(format))

    conn.close()

    while True:
      conn, addr = server.accept()
      thread = threading.Thread(target = helper, args = (conn, addr))
      thread.start()


