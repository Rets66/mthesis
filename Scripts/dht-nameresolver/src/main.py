#/usr/env python3
#encoding: utf-8

import csv
import hashlib
import os
import socket
import socketserver
import sys
import threading

from redis import Redis
from twisted.names import dns, server
from twisted.python import log

SALT = ["repli", "repli2"]
DB_ADDR = ["localhost", xxx]


class PutHandler(socketserver.BaseRequestHandler):
    def __init__(self, content, table):
        self.content = content
        self.table = []
        with open('/etc/ddns/table.csv', newline='') as f:
            reader = csv.reader(f)
            for i in reader:
                self.table.append(i)

    def handle(self):
        data = self.request.recv(1024)
        value = data[]

    def calc_key(self, name, rtype, salt):
        query = [name + rtype]
        queries += [name + rtype + i for i in salt]
        bin_query = [bytes(i, encoding='utf-8') for i in queries]
        content_id = [hashlib.sha3_256(i).hexdigest() for i in bin_query]
        return content_id

    def find_manager(self, target):
        start = [i[0] for i in self.table]
        start.append(target).sort()
        node = start.index(target) - 1
        return table[node]

    def request(self, dst, content):
        addr = (dst[2], 8080)        # dst = [start, end, address, name]
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(addr)
            s.sendall(content.encode())


class StoreHandler(socketserver.BaseRequestHandler):
    def __init__(self):
        DatabaseHandler().start()

    def handle(self, value):
        data = self.request.recv(1024)
        value = data[].split(',')
        name, rtype, record_value = value[0], value[1], value[2:]

    def store(self, dst):
        self.dst = dst
        DatabaseHandle().store(self.dst)


class NameQueryHandler:
    def __init__(self):
        self.factory = server.DNSServerFactory(
            clients=[client.Resolver(resolv='/etc/resolv.conf')]
        )
        self.protocol = dns.DNSDatagramProtocol(controller=self.factory)

    def log(self):
        log.startLogging(sys.stderr)

    def serve(self):
        reactor.listenUDP(10053, self.protocol)
        reactor.listenTCP(10053, self.factory)
        reactor.run()

    def lookup(self, key):
        r = Redis(host=DB_ADDR[0], port=DB_ADDR[1])
        value = r.get(key)
        if value:
            return value
        else:
            raise pass # Error Record

    def response(self, value):pass


class DatabaseHandler:
    def start(self):pass

    def store(self, key, value):
        r = Redis(host='', port='')
        r.set(key, value)

    def delete(self, key):pass





if __name__ == '__main__':
    os.mkdir('/etc/ddns')
