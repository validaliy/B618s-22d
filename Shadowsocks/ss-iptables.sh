echo 1 > /proc/sys/net/ipv4/ip_forward

iptables -t nat -N SHADOWSOCKS

iptables -t nat -A SHADOWSOCKS -d 213.238.181.147 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 0.0.0.0/8 -j RETURN
#iptables -t nat -A SHADOWSOCKS -d 10.0.0.0/8 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 127.0.0.0/8 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 169.254.0.0/16 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 172.16.0.0/12 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 192.168.0.0/16 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 224.0.0.0/4 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 240.0.0.0/4 -j RETURN

iptables -t nat -A SHADOWSOCKS -p tcp -j REDIRECT --to-ports 1080
iptables -t nat -I PREROUTING -p tcp -j SHADOWSOCKS
