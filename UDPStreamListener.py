#!/usr/bin/env python3


class UDPStreamListener:

    def __init__(self, host, port):
        self.host_ = host
        self.check_sum = port

    def tostring(self):
        print("My name is: %s\nMy occupation is: %s" % (self.issue, self.check_sum))

    def perticipateToStream(self):
        print("listen to multicast stream")