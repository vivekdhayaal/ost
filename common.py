from keystoneclient.v3 import client

import numpy as np

import datetime

import conf

USERNAME='admin'
PASSWORD='nova'
PROJECT_NAME='admin'
KEYSTONE_URL='http://172.31.25.80:5000/v3'
USER_DOMAIN_NAME='Default'
PROJECT_DOMAIN_NAME='Default'
ITERATIONS=300

ks = client.Client(username=conf.USERNAME, password=conf.PASSWORD,
        project_name=conf.PROJECT_NAME,
        project_domain_name=conf.PROJECT_DOMAIN_NAME,
        user_domain_name=conf.USER_DOMAIN_NAME,
        auth_url=conf.KEYSTONE_URL)

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

