from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy

import uuid

cluster = Cluster(['52.74.170.193', '52.74.230.111', '54.169.112.143', '54.169.89.81', '52.74.161.193'],
    load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='DC2'),
    protocol_version=3
    )

session = cluster.connect()
session.set_keyspace('keystone')
#print session.execute('select * from project limit 1;')
#future = session.execute_async("insert into project (id, description, domain_id, enabled, extra, name, parent_id) values ('pk', 'desc', 'domid', True, '{}', 'projname', '');")

futures = []

def get_futures(session):
    id = uuid.uuid4().hex
    future1 = session.execute_async("insert into project (id, description, domain_id, enabled, extra, name, parent_id) values ('%s', 'desc', 'default', True, '{}', 'test-%s', '');"%(id, id))
    future2 = session.execute_async("insert into project_gsi_name_domain_id (name, domain_id, project_id) values ('test-%s', 'default', '%s');"%(id, id))
    global futures
    futures.append(future1)
    futures.append(future2)

for i in range(100000):
    get_futures(session)

for future in futures:
    future.result()

#def callback_done():
#    print 'done'
#
#def log_results(results):
#    print 'ok'
#    #for row in results:
#    #    print("Results: %s", row)
#
#def log_error(exc):
#    #import pdb;pdb.set_trace()
#    print("Operation failed: %s", exc)

#future.add_callbacks(log_results, log_error)

#import time;time.sleep(10)
cluster.shutdown()
