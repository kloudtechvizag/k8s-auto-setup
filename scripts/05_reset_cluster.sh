#!/bin/bash
CLUSTER_NAME=$(cat config/cluster_name.txt 2>/dev/null || echo "mycluster")
cd kubespray

ansible-playbook -i inventory/$CLUSTER_NAME/hosts.yaml --become reset.yml
