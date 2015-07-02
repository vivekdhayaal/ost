from keystoneclient.v3 import client

import datetime

USERNAME='admin'
PASSWORD='nova'
PROJECT_NAME='admin'
KEYSTONE_URL='http://10.0.2.15:5000/v3'
USER_DOMAIN_NAME='Default'
PROJECT_DOMAIN_NAME='Default'

ks = client.Client(username=USERNAME, password=PASSWORD, project_name=PROJECT_NAME,
        project_domain_name=PROJECT_DOMAIN_NAME, user_domain_name=USER_DOMAIN_NAME,
        auth_url=KEYSTONE_URL)

resp_times = []

for i in range(1000):
    start = datetime.datetime.utcnow()
    ks.users.list()
    end = datetime.datetime.utcnow()
    resp_times.append((end-start).total_seconds())


print resp_times
#for i in resp_times:
#    print i
