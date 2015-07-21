import common
from datetime import datetime

import uuid

ks = common.ks
projects = []
start=datetime.utcnow()
for i in range(10000):
    projects.append(ks.projects.create(
            name='revoketest-'+str(i+1),
            domain='default',
            description='test tenant',
            enabled=True))
end=datetime.utcnow()
print('Time taken to create 10000 tenants: ', (end-start).total_seconds(), ' seconds')

start=datetime.utcnow()
for i in range(1000):
    ks.projects.delete(projects[i])
end=datetime.utcnow()
print('Time taken to delete 1000 tenants: ', (end-start).total_seconds(), ' seconds')
