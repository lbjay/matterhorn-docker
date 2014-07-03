#!/usr/bin/env bash

apt-get update
apt-get install -y python-pip python-dev curl
curl -s https://get.docker.io/ubuntu/ | sudo sh
pip install fabric
sudo usermod -a -G docker vagrant
