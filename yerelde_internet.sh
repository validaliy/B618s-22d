#!/bin/sh

# Belirtilen IP adresi yani vpsnin ip adresi
SPECIFIC_IP="213.238.181.147"

# Yeni IP adresi
IPADDRESS=$(ifconfig eth_x | grep "inet " | awk '{print $2}' | awk -F: '{print $2}')

# Belirtilen IP adresinden çıkan trafiği kontrol etmek için bir kuralı en başa ekle
iptables -t nat -I OUTPUT 1 -s $IPADDRESS -d ! $SPECIFIC_IP -p tcp -j REDIRECT --to-port 1080