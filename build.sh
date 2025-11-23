#!/bin/bash

apt-get update
apt-get install -y curl autoconf automake libtool pkg-config

cd /tmp
git clone https://github.com/openvenues/libpostal
cd libpostal


./bootstrap.sh
./configure --datadir=/opt/libpostal_data
make -j4

make install
ldconfig

pip install postal

