# flightsim-controller
Pi zero based controller that emulates a keyboard.  Building it to use as a flight simulator control box.  Currently I'm building it to work with FlightGear, but the keys are configurable in the code so it should be adaptable to any other FS as well.

## Instructions to configure Raspberry Pi zero as a USB gadget
https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/

## Install the program to auto-run at boot up
Add the following like to the `/etc/rc.local` file.

```(cd /home/pi/flightsim-controller/;./run.sh)```

