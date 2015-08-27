#!/bin/bash
set -x
for i in {105501..106000}
do
    #keystone user-create --name vivek$i --tenant demo --pass vivek$i
    #openstack user create vivek$i --project demo --password vivek
    #curl -d '{"auth":{"passwordCredentials":{"username": "vivek'$i'", "password": "vivek"},"tenantName": "demo"}}' -H "Content-Type: application/json" http://172.31.25.98:5000/v2.0/tokens &
    /usr/bin/time -f "%e" -o token-get-log.txt -a curl -d '{"auth":{"passwordCredentials":{"username": "vivek'$i'", "password": "vivek"},"tenantName": "demo"}}' -H "Content-Type: application/json" http://172.31.25.98:5000/v2.0/tokens &
    #time keystone user-list
    #( time curl -H "X-Auth-Token: fbce59418f984e69afe25ddeb012e50b" http://172.31.25.98:5000/v3/users ) |& tee n.log
    #time curl -H "X-Auth-Token: fbce59418f984e69afe25ddeb012e50b" http://172.31.25.98:5000/v3/users -o |& tee n.log
    #time curl -H "X-Auth-Token: fbce59418f984e69afe25ddeb012e50b" http://172.31.25.98:5000/v3/users
    #echo "==================================================================" >> c.log
    #echo "=================================================================="
done
wait
