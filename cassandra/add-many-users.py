from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy

import uuid

cluster = Cluster(['52.74.170.193', '52.74.230.111', '54.169.112.143', '54.169.89.81', '52.74.161.193'],
    load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='DC2'),
    protocol_version=3
    )

session = cluster.connect()
session.set_keyspace('keystone33')


def create_users(session, id):
    future1 = session.execute_async("INSERT INTO user (id, default_project_id, domain_id, enabled, extra, name, password) VALUES ('%s', NULL, 'default', True, '{\"email\": null}', 'user-%s', '$6$rounds=40000$mYA6Iwpl6dm.ijML$swgnT0JM/lLoagtwnY.JL/e24TRh97koMIO/Gx9tDHajzeZpuEXQKLcYJ0.DQoVxIpCCPV0xKME6llo73oqhz/');"%(id, id))
    future2 = session.execute_async("INSERT INTO domain_id_user_name_to_user_id (domain_id, name, user_id) VALUES ( 'default', 'user-%s', '%s');"%(id, id))
    global futures
    futures.append(future1)
    futures.append(future2)

# Insert 100 million users!
for j in range(1000):
    futures = []
    print j
    for i in range(100000):
        create_users(session, 100000*j+i)
    for future in futures:
        future.result()
    del futures


cluster.shutdown()
