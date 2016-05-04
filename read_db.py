#!/usr/bin/env python
from testdb import db
from testdb import Spoon
'''
new_host = Spoon('hostname', 'ip_addr', 'username', 'password')
db.session.add(new_host)
db.session.commit()
'''

hosts = Spoon.query.all()
print hosts
print hosts[0].ip_addr
