#!/system/bin/busyboxx sh
SPECIFIC_IP="213.238.181.147"
IPADDRESS=$(ifconfig eth_x | grep "inet " | awk '{print $2}' | awk -F: '{print $2}')
iptables -t nat -I OUTPUT 1 -s $IPADDRESS -d ! $SPECIFIC_IP -p tcp -j REDIRECT --to-port 1080
