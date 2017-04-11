#!/usr/bin/env python3
import socket
import struct


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
            w = ord(msg[i]) + (ord(msg[i + 1]) << 8)
            s = self.__carry_around_add(s, w)
        return ~s & 0xffff

    def join_multicast_stream(self):
        print("joinging stream")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host_ip, self.host_port))

        data, addr = self.sock.recvfrom(1024)
        print('data ', data)

        # while True:
        #      data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes
        #      data = list(map(lambda x: int(x,16), data.split()))
        #      data = struct.pack("%dB" % len(data), *data)
        #      print('Checksum: ', self.__checksum(data))
