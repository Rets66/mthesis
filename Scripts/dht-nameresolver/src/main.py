#/usr/env python3

import csv
import hashlib
import os
import socket

from redis import Redis
from twisted.names import client, dns, server

SALT = ["agent", "agent2"]
REDIS_ADDR = {"host":"localhost", "port":xxx}


class StoringHandler():
    """
    key = sha3(name+rr(salt))
    value = '"name", "rr", "record value"'
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def listen(self):pass

    def parser(self, value):
        parsed_value = self.value.split(',')
        name = parsed_value[0]
        rr = parsed_value[1]
        record_value = parsed_value[2:]
        return qname, rr, record_value

    def start_redis(self):pass

    def store(self, key, value):
        r = Redis(host='', port='')
        r.set(key, value)


class StoreRequestHandler():
    def __init__(self, content, table):
        self.content = content
        self.table = []
        with open('/etc/ddns/table.csv', newline='') as f:
            reader = csv.reader(f)
            for i in reader:
                self.table.append(i)

    def hash(self, qname, rr):
        self.qname = qname
        self.rr = rr

        query = self.qname + self.rr
        query_key = hashlib.sha3_256(query.encode()).hexdigest()
        spare = [query + salt[i] for i in range(2)]
        key = [hashlib.sha3_256(i.encode()).hexdigest() for i in spare]
        key.insert(0, query_key)
        return key

    def find_dst(self, table, target):
        start = [i[0] for i in table]
        start.append(target).sort()
        node = start.index(target) - 1
        return table[node]

    def requests(self, dst, content):
        addr = (dst[2], 8080)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(addr)
            s.sendall(content.encode())


class LookUpAgent():
    def __init__(self, key):
        self.key = key

    def handle_query(self):pass # from Full-service resolver

    def lookup(self, key):
        r = Redis(host=REDIS_ADDR["host"], port=REDIS_ADDR["port"])
        value = r.get(key)
        return value

    def response(self):pass # to client



if __name__ == '__main__':
    os.mkdir('/etc/ddns', )
