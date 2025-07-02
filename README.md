# 🚀 Kubespray Automated Kubernetes Cluster Setup

This project automates the provisioning of a **production-ready Kubernetes cluster using Kubespray** and Ansible. With just a few simple config files and one command, you can set up a Kubernetes cluster across any number of Linux nodes.

---

## 📦 What's Included?

- 🔁 Automatic inventory generation from IP list
- 🔑 SSH key distribution to all cluster nodes
- ⚙️ Kubespray clone and dependency installation
- ⛓️ One-click cluster provisioning
- 📂 Kubeconfig retrieval for local access
- 🔄 Cluster reset option

---

## 🧱 Directory Structure

```
kubespray-auto-cluster/
├── config/
│   ├── node_ips.txt          # List of node IPs (one per line)
│   ├── ssh_user.txt          # SSH username (e.g. ubuntu)
│   ├── ssh_key.pub           # Public SSH key for access
│   └── cluster_name.txt      # Optional cluster name
├── scripts/
│   ├── 01_generate_inventory.py
│   ├── 02_copy_ssh_key.sh
│   ├── 03_run_kubespray.sh
│   ├── 04_get_kubeconfig.sh
│   └── 05_reset_cluster.sh
├── setup.sh                  # Main setup launcher
├── kubespray/                # Cloned Kubespray repo (auto-created)
└── README.md
```

---

## ⚙️ Prerequisites

- A control machine with:
  - Ubuntu/Debian/CentOS
  - Python 3 and pip
  - `git`, `sshpass`, `scp`, `ansible`
- Target nodes:
  - Ubuntu/Debian/CentOS
  - SSH access enabled
  - Python installed
  - IP addresses reachable from the control machine

---

## 🚀 Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/yourname/kubespray-auto-cluster.git
cd kubespray-auto-cluster
```

### 2. Configure Your Cluster

#### `config/node_ips.txt`

```txt
192.168.56.101
192.168.56.102
192.168.56.103
```

> First node is assumed to be master (control plane), others are workers.

#### `config/ssh_user.txt`

```txt
ubuntu
```

#### `config/ssh_key.pub`

Paste your SSH public key here.

Generate one with:

```bash
ssh-keygen -t rsa -b 4096
cat ~/.ssh/id_rsa.pub > config/ssh_key.pub
```

#### Optional: `config/cluster_name.txt`

```txt
mycluster
```

---

### 3. Launch the Setup

```bash
chmod +x setup.sh scripts/*.sh
./setup.sh
```

This will:
- Clone Kubespray
- Install dependencies
- Generate Ansible inventory
- Distribute SSH keys
- Run `cluster.yml` via Ansible
- Fetch kubeconfig for local access

---

## 🧪 Validate Cluster

```bash
export KUBECONFIG=$(pwd)/kubeconfig
kubectl get nodes
kubectl get pods -A
```

---

## 🔁 Resetting the Cluster

To tear down the cluster and clean up:

```bash
bash scripts/05_reset_cluster.sh
```

---

## 🛠️ Customization

You can customize your Kubernetes setup by editing:

```bash
kubespray/inventory/<your-cluster>/group_vars/k8s_cluster/k8s-cluster.yml
```

Some options include:
- Network plugin (`calico`, `flannel`, `cilium`)
- Enable ingress controllers
- Change pod network CIDRs
- Add HA masters and etcd nodes

---

## 📌 Notes

- Ensure your SSH key is distributed or SSH agent is running for seamless login.
- For better security, modify `scripts/02_copy_ssh_key.sh` to prompt for passwords or use `ssh-agent`.
- HA setup is supported: just list multiple master IPs and modify inventory script accordingly.

---

## 📚 References

- [Kubespray GitHub](https://github.com/kubernetes-sigs/kubespray)
- [Kubernetes Docs](https://kubernetes.io/docs/)
- [Ansible Docs](https://docs.ansible.com/)

---

## 🤝 Contributing

Feel free to fork this project and add:
- HA support
- Cloud-specific support (e.g., AWS, GCP)
- SSH agent integration
- Post-install Helm setup

---

## 📜 License

MIT License – Use freely for both personal and commercial projects.
