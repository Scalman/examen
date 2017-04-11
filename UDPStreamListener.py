#!/usr/bin/env python3
import socket
import struct

class UDPStreamListener:

    def __init__(self, host, port):
        self.host_ = host
        self.check_sum = port

    def tostring(self):
        print("My name is: %s\nMy occupation is: %s" % (self.issue, self.check_sum))

    def perticipateToStream(self):
        print("listen to multicast stream")
        UDP_IP = '233.12.166.100'
        UDP_PORT = 1234
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))

        while True:
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            #print "received message:", data
            data = data.split()
            data = map(lambda x: int(x,16), data)
            data = struct.pack("%dB" % len(data), *data)
            #print ' '.join('%02X' % ord(x) for x in data)
            #print 'Checksum: '
            # #, checksum(data)