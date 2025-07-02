import yaml
from pathlib import Path

with open("config/node_ips.txt") as f:
    ips = [line.strip() for line in f if line.strip()]

with open("config/ssh_user.txt") as f:
    ssh_user = f.read().strip()

cluster_name = Path("config/cluster_name.txt").read_text().strip() if Path("config/cluster_name.txt").exists() else "mycluster"
inventory_path = f"kubespray/inventory/{cluster_name}"
hosts_file = Path(f"{inventory_path}/hosts.yaml")
hosts_file.parent.mkdir(parents=True, exist_ok=True)

all_hosts = {
    "all": {
        "hosts": {},
        "children": {
            "kube_control_plane": {"hosts": {}},
            "kube_node": {"hosts": {}},
            "etcd": {"hosts": {}},
            "k8s_cluster": {"children": {"kube_control_plane": {}, "kube_node": {}}},
            "calico_rr": {"hosts": {}},
        },
    }
}

for i, ip in enumerate(ips):
    name = f"node{i+1}"
    all_hosts["all"]["hosts"][name] = {
        "ansible_host": ip,
        "ip": ip,
        "access_ip": ip,
        "ansible_user": ssh_user,
    }
    all_hosts["all"]["children"]["kube_control_plane"]["hosts"][name] = {}
    all_hosts["all"]["children"]["kube_node"]["hosts"][name] = {}
    all_hosts["all"]["children"]["etcd"]["hosts"][name] = {}

with open(hosts_file, "w") as f:
    yaml.dump(all_hosts, f, default_flow_style=False)

print(f"✅ Inventory written to {hosts_file}")
