#!/usr/bin/env python
from flask import Flask
from testdb import db
from testdb import Spoon

hosts = Spoon.query.all()
d = {}
j = 0
for i in hosts:
    print '-'* 25
    print i
    print i.hostname
    print i.ip_addr
    print i.username
    print i.password
    d[j] = {}
    d[j]['hostname'] = i.hostname
    d[j]['ip_addr'] = i.ip_addr
    d[j]['username'] = i.username
    d[j]['password'] = i.password
    j = j + 1

print ""
print d
