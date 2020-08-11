#!/bin/bash

echo "Install dependencies"
echo "Installing py-gaugette and its dependencies"
echo "   Installing wiringpi"
sudo pip install wiringpi

echo "   Installing py-gaugette"
curr_dir=`pwd`
cd ~
git clone git://github.com/guyc/py-gaugette.git
cd py-gaugette
sudo python setup.py install
cd $curr_dir
