import common
from datetime import datetime

import uuid

ks = common.ks

start=datetime.utcnow()
for i in range(1000):
    ks.projects.create(
            name='test-'+uuid.uuid4().hex,
            domain='default',
            description='test tenant',
            enabled=True)
end=datetime.utcnow()
print('Time taken to create 1000 tenants: ', (end-start).total_seconds(), ' seconds')
