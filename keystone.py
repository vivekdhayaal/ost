from keystoneclient.v3 import client

import numpy as np

import datetime

USERNAME='admin'
PASSWORD='nova'
PROJECT_NAME='admin'
KEYSTONE_URL='http://172.31.25.80:5000/v3'
USER_DOMAIN_NAME='Default'
PROJECT_DOMAIN_NAME='Default'
ITERATIONS=100

ks = client.Client(username=USERNAME, password=PASSWORD,
        project_name=PROJECT_NAME,
        project_domain_name=PROJECT_DOMAIN_NAME,
        user_domain_name=USER_DOMAIN_NAME,
        auth_url=KEYSTONE_URL)

def get_response_times(method, *args):
    resp_times = []

    for i in range(ITERATIONS+100):
        # Let us warm up a little
        if i < 100:
            method(*args)
            continue

        start = datetime.datetime.utcnow()
        method(*args)
        end = datetime.datetime.utcnow()
        resp_times.append((end-start).total_seconds())

    avg = sum(resp_times)/len(resp_times)*1000
    p95 = np.percentile(resp_times, 95)*1000
    p99 = np.percentile(resp_times, 99)*1000
    del(resp_times) # Required really?
    return (avg, p95, p99)

print('List a user')
user_name = ks.users.list()[0].id
print get_response_times(ks.users.get, user_name)

print('List all user')
print get_response_times(ks.users.list)
