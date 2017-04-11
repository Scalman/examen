#!/usr/bin/env python3
import socket
import struct
import time
import binascii

class UDPStreamListener:

    def __init__(self, host_ip, host_port):
        self.host_ip = host_ip #233.12.166.100
        self.host_port = host_port #1234
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def to_string(self):
        print('My name is: %s\nMy occupation is: %s', (self.host_ip, self.host_port))

    def __carry_around_add(self, a, b):
        c = a + b
        return (c & 0xffff) + (c >> 16)

    def __checksum(self, msg):
        s = 0
        for i in range(0, len(msg), 2):
            w = (msg[i]) + (msg[i + 1] << 8)
            s = self.__carry_around_add(s, w)
        return ~s & 0xffff

    def join_multicast_stream(self):
        print("joining stream")

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host_ip, self.host_port))

        mreq = struct.pack("4sl", socket.inet_aton(self.host_ip), socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        data, addr = self.sock.recvfrom(2048)
        data = binascii.hexlify(data).decode()
        data = [data[i: i+2] for i in range(0, len(data), 2)]
        data = list(map(lambda x: int(x, 16), data))
        print('Checksum: 0x%04x' % self.__checksum(data))

        # while True:
        #      data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes
        #      data = list(map(lambda x: int(x,16), data.split('\')))
        #      data = struct.pack("%dB" % len(data), *data)
        #      print('Checksum: ', self.__checksum(data))
