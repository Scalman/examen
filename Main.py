#!/usr/bin/env python3

from UDPStreamListener import UDPStreamListener


def main():
    udp_listener = UDPStreamListener('233.12.166.100', 1234)
    udp_listener.join_multicast_stream()

if __name__ == "__main__":
    main()
