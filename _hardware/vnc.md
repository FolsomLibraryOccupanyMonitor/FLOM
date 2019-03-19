To set up remote access to a Raspberry Pi follow these steps:
This link has additional details to this one.
https://www.raspberrypi.org/documentation/remote-access/vnc/
1. Go on the terminal and type
sudo apt-get update
sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer
2. Enable VNC server on the command line.
sudo raspi-config and select Yes for vnc
3. Get the ip address that the raspberry pi is connected to in the terminal by typing sudo hostname -I. Type this ip address into the VNC viewer search, and connect to it.
4. Make a VNC viewer account and you should be connected. You should be able to access
the raspberry pi on your laptop and even some mobile devices.

You can set up a free vnc viewer account at this link:
https://www.realvnc.com/en/
