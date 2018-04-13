#!/bin/sh

set -ex
sudo apt-get update
sudo apt-get install ruby-dev build-essential p7zip-full rpm gdb libudev-dev qt5-default
sudo apt-get remove libusb-1.0-0
curl -L -O https://kent.dl.sourceforge.net/project/libusb/libusb-1.0/libusb-1.0.21/libusb-1.0.21.tar.bz2
tar xjf libusb-1.0.21.tar.bz2
(cd libusb-1.0.21 && ./configure --prefix=/usr && make && sudo make install)
gem install fpm
pip3 install -r src/requirements.txt
pip3 install -r src/requirements-${TRAVIS_OS_NAME}.txt

.travis/install-phidgets.sh
.travis/install-snap7.sh
.travis/install-pymodbus.sh
