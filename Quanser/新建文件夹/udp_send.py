import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.sendto('0'.encode('utf-8'), ("192.168.31.51", 4096))
udp_socket.close()
