### All nodes:
```
hostnamectl set-hostname node1.ibar.az
```
```
swapoff -a
```
```
nano /etc/fstab and comment swap
```
```
INSTALL DOCKER
```
```
sudo apt-get update && sudo apt-get install -y apt-transport-https curl
```
```
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
```
```
cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
```
```
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
```

### Master node:
```
sudo kubeadm init --pod-network-cidr=10.244.0.0/16 --apiserver-advertise-address=172.31.5.150
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/2140ac876ef134e0ed5af15c65e414cf26827915/Documentation/kube-flannel.yml
```
