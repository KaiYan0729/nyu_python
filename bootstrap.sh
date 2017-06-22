#!/usr/bin/env bash

apt-get install build-essential gcc --assume-yes
apt-get update --fix-missing
apt-get install vim git --assume-yes
apt-get install vim git python3 --assume-yes
apt-get install vim git python3-venv --assume-yes

apt-get install bpython --assume-yes

###su - vagrant -c "cd /home/vagrant && mkdir dev && cd dev && git clone https://github.com/robmarano/nyu-python.git"
