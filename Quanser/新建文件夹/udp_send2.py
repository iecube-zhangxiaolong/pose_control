import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.sendto('1'.encode('utf-8'), ("192.168.8.144", 4097))
udp_socket.close()
