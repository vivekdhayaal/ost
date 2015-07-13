from keystoneclient.v3 import client

import numpy as np

import datetime

USERNAME='admin'
PASSWORD='nova'
PROJECT_NAME='admin'
KEYSTONE_URL='http://172.31.25.80:5000/v3'
USER_DOMAIN_NAME='Default'
PROJECT_DOMAIN_NAME='Default'
ITERATIONS=300

ks = client.Client(username=USERNAME, password=PASSWORD,
        project_name=PROJECT_NAME,
        project_domain_name=PROJECT_DOMAIN_NAME,
        user_domain_name=USER_DOMAIN_NAME,
        auth_url=KEYSTONE_URL)


