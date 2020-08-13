#!/bin/bash

echo "Install dependencies"
echo "Installing py-gaugette and its dependencies"
echo "   Installing wiringpi via pip"
sudo pip3 install wiringpi
echo "   Installing wiringpi via apt"
sudo apt-get install wiringpi

echo "   Installing py-gaugette"
#curr_dir=`pwd`
#cd ~
git clone git://github.com/guyc/py-gaugette.git
ln -s py-gaugette/gaugette gaugette
#cd py-gaugette
#sudo python setup.py install
#cd $curr_dir
