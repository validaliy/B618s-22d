export SSIP=127.0.0.1
export SSRP=2080
SSPASS="asdasd"
SSMETHOD="chacha20"

/online/opt/bin/ss-redir -s $SSIP -p $SSRP -b 0.0.0.0 -l 1080 -k $SSPASS -m $SSMETHOD -t 600 -f /var/run/shadowsocks.pid &
/online/ss-iptables.sh
