from keystoneclient.v3 import client

import numpy as np

import datetime

USERNAME='admin'
PASSWORD='nova'
PROJECT_NAME='admin'
KEYSTONE_URL='http://172.31.25.98:5000/v3'
USER_DOMAIN_NAME='Default'
PROJECT_DOMAIN_NAME='Default'

ks = client.Client(username=USERNAME, password=PASSWORD,
        project_name=PROJECT_NAME,
        project_domain_name=PROJECT_DOMAIN_NAME,
        user_domain_name=USER_DOMAIN_NAME,
        auth_url=KEYSTONE_URL)

resp_times = []

for i in range(100):
    start = datetime.datetime.utcnow()
    ks.users.list()
    end = datetime.datetime.utcnow()
    #print (end-start).total_seconds()
    resp_times.append((end-start).total_seconds())

print 'Average:', sum(resp_times)/len(resp_times)
print '95th %:', np.percentile(resp_times, 95)

resp_times=[]

for i in range(100):
    start = datetime.datetime.utcnow()
    ks.users.get('cf1f87101f8d4e8a92dc8a5a7cfa319e')
    end = datetime.datetime.utcnow()
    #print (end-start).total_seconds()
    resp_times.append((end-start).total_seconds())


print 'Average:', sum(resp_times)/len(resp_times)
print '95th %:', np.percentile(resp_times, 95)
