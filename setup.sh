#!/bin/sh
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done

sudo apt-get -y update
sudo apt-get -y install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get -y update

sudo apt-get install -y docker-ce
sudo apt-get install -y docker-ce-cli
sudo apt-get install -y containerd.io
sudo apt-get install -y docker-buildx-plugin
sudo apt-get install -y docker-compose-plugin

sudo systemctl enable docker

sudo groupadd docker
sudo usermod -aG docker $USER
sudo chown $USER /var/run/docker.sock
newgrp docker

docker run -v ./backend/db/init.sh:/init.sh --env-file .env --rm postgres:latest ./init.sh
docker rmi $(docker images 'postgres' -a -q)