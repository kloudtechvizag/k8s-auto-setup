#!/bin/bash
set -e

# Clone Kubespray if not already
if [ ! -d kubespray ]; then
  git clone https://github.com/kubernetes-sigs/kubespray.git
fi

cd kubespray
pip install -r requirements.txt
cd ..

# Generate inventory
python3 scripts/01_generate_inventory.py

# Setup SSH
bash scripts/02_copy_ssh_key.sh

# Run Kubespray
bash scripts/03_run_kubespray.sh

# Get kubeconfig
bash scripts/04_get_kubeconfig.sh
