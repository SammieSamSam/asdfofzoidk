#!/bin/bash

NADHOC="# interfaces(5) file used by ifup(8) and ifdown(8)

# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d"

ADHOC="# interfaces(5) file used by ifup(8) and ifdown(8)

# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d

auto lo
iface lo inet loopback

iface eth0 inet dhcp

auto wlan0
iface wlan0 inet static
	address 123.167.1.2
	netmask 255.255.255.0
	wireless-channel 1
	wireless-essid rpinet
	wireless-mode ad-hoc"

systemctl stop dhcpcd.service

if [ "$1" == "true" ]
	then
		echo "Ad-Hoc network is set to true."
		cat > /etc/network/interfaces << _EOF_
		$ADHOC
_EOF_
elif [ "$1" == "false" ]
	then
		echo "Ad-Hoc network is set to false."
		cat > /etc/network/interfaces << _EOF_
		$NADHOC
_EOF_
fi

read -p "The computer needs to reboot for the changes to take effect, do you want to restart now? (y/n): " confirm 
if [ "$confirm" == "y" ]
	then
		reboot -h now
fi

exit 0