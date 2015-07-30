from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy

import uuid
from datetime import datetime
import random

import numpy as np

cluster = Cluster(['52.74.170.193', '52.74.230.111', '54.169.112.143', '54.169.89.81', '52.74.161.193'],
    load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='DC2'),
    protocol_version=3
    )

session = cluster.connect()
session.set_keyspace('keystone33')

# ID of the user is between 0 and 15099999
START_INDEX=0
END_INDEX=15099999

start_time=None
end_time=None

def a():
    global start_time
    start_time=datetime.utcnow()

def z():
    global start_time
    global end_time
    end_time=datetime.utcnow()
    return (end_time-start_time).total_seconds()*1000


def list_random_user():
    random_index = random.randint(START_INDEX, END_INDEX)
    a()
    row = session.execute("select * from user where id='%s'"%(random_index))
    return z()

resp_times = []
for i in range(10000):
    resp_times.append(list_random_user())

print 'avg:', sum(resp_times)/len(resp_times)
print '99 perc:', np.percentile(resp_times, 99)
print '95 perc:', np.percentile(resp_times, 95)
print 'median:', np.percentile(resp_times, 50)

cluster.shutdown()
