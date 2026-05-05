#!/usr/bin/env bash
set -euo pipefail

sudo dnf update -y || true
sudo dnf install -y git curl wget vim jq docker || true
sudo systemctl enable --now docker || true
sudo usermod -aG docker "$USER" || true

curl -sfL https://get.k3s.io | sh -
mkdir -p ~/.kube
sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
sudo chown "$USER:$USER" ~/.kube/config

curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

echo "k3s and Helm installed. Log out/in if Docker group permissions are not active."
