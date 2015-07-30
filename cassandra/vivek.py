from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
from datetime import datetime

import uuid

cluster = Cluster(['52.74.199.243', '52.74.21.93', '54.169.159.205'],
    load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='dc3'),
    protocol_version=3
    )

session = cluster.connect()
session.set_keyspace('keystone')
#print session.execute('select * from project limit 1;')
#print session.execute('select * from project;')
#future = session.execute_async("insert into project (id, description, domain_id, enabled, extra, name, parent_id) values ('pk', 'desc', 'domid', True, '{}', 'projname', '');")

futures = []

def get_futures_proj(id):
    future1 = session.execute_async("insert into project (id, description, domain_id, enabled, extra, name, parent_id) values ('%s', 'desc', 'default', True, '{}', '%s', '');"%(id,id))
    future2 = session.execute_async("insert into project_gsi_name_domain_id (name, domain_id, project_id) values ('%s', 'default', '%s');"%(id,id))
    global futures
    futures.append(future1)
    futures.append(future2)

user_f = []
def get_futures_sql(sql):
    user_f.append(session.execute_async(sql))
    #session.execute_async(sql)

#for i in xrange(31, 10031):
#    user_sql = "INSERT INTO user (id,default_project_id,domain_id,enabled,extra,name,password) VALUES ( 'vivek%s', null, 'default', True, '{}', 'vivek%s', '$6$rounds=40000$LNubhvjGuopgfBc5$CYDCqEpdysTW9UdWUf8dofLZMy65V.kxa26fgMIJagQ9MjNwvTJn54csgZKZlZEaBnYHSr5IRq4Cz8dcpfQVG1');" % (str(i), str(i))
#    get_futures_sql(user_sql)

#for future in user_f:
#    future.result()

for k in xrange(2, 602, 10):
    start=datetime.utcnow()
    for i in xrange(k, k+10):
        proj_id = 'vivekpp' + str(i*1000)
        get_futures_proj(proj_id)
        for j in xrange(31, 10031):
            user_sql = "INSERT INTO role_assignment (type, actor_id, target_id, role_id, inherited) VALUES ( 'UserProject', '%s', '%s', '9fe2ff9ee4384b1894a90878d3e92bab', False);" % ('vivek' + str(j), proj_id)
            get_futures_sql(user_sql)
    end=datetime.utcnow()
    print('Time taken to execute_async 100000 role_assignments : ', (end-start).total_seconds(), ' seconds')
    start=datetime.utcnow()
    for future in futures:
        future.result()
    futures = []
    for future in user_f:
        future.result()
    user_f = []
    end=datetime.utcnow()
    print('Time taken to future.result 100000 role_assignments : ', (end-start).total_seconds(), ' seconds')

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

