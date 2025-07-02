#!/bin/bash
MASTER_IP=$(head -n 1 config/node_ips.txt)
USER=$(cat config/ssh_user.txt)

scp "$USER@$MASTER_IP:/etc/kubernetes/admin.conf" ./kubeconfig
echo "✅ Run this to use the cluster:"
echo "export KUBECONFIG=$(pwd)/kubeconfig"
