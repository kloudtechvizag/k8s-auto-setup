#!/bin/bash
set -e

USER=$(cat config/ssh_user.txt)
PUBKEY=$(cat config/ssh_key.pub)

while read -r ip; do
    echo "Copying SSH key to $USER@$ip ..."
    sshpass -p 'your_password_here' ssh-copy-id -o StrictHostKeyChecking=no "$USER@$ip"
done < config/node_ips.txt
