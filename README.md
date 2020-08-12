# flightsim-controller
Pi zero based controller that emulates a keyboard.  Building it to use as a flight simulator control box.  Currently I'm building it to work with FlightGear, but the keys are configurable in the code so it should be adaptable to any other FS as well.

## Instructions to configure Raspberry Pi zero as a USB gadget
https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/

### Rotary encoder
The rotary encoder code is using the instructions found at:

https://guy.carpenter.id.au/gaugette/blog/2013/01/14/rotary-encoder-library-for-the-raspberry-pi/

However the code in it is for an older version of py-gaugette.  This code has been modified to the current version (as of Aug 2020) of py-gaugette.

https://github.com/guyc/py-gaugette

## Setup
Run the following command to install dependencies required.
```./setup.sh```

## Install the program to auto-run at boot up
Add the following like to the `/etc/rc.local` file.

```(cd /home/pi/flightsim-controller/;./run.sh)```

