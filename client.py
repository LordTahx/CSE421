import socket
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

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(client)
client.connect(server_socket_address)
print(client)

def msg_to_be_sent(msg):
    message = msg.encode(format)	
    msg_length = len(message)
    msg_length = str(msg_length).encode(format)
    msg_length += b" " * (buffer-len(msg_length))

    client.send(msg_length)
    client.send(message)
    print(client.recv(2048).decode(format))

msg_to_be_sent(f"IP address of the client is {host_ip_address} and the device name is {hostname}")
msg_to_be_sent("Apple")
msg_to_be_sent("Proyas gay")
msg_to_be_sent("nandu kala para na")
msg_to_be_sent(disconnected)

