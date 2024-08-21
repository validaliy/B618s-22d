#!/system/bin/busyboxx sh

# /opt/baslangic.sh

# kisayollar
busybox ln -sf /opt/bin/nano /bin/nano
busybox ln -sf /opt/bin/opkg /bin/opkg
busybox ln -sf /opt/bin/stunnel /bin/stunnel


busybox ln -sf /system/bin/busybox-armv7l netstat /bin/netstat
busybox ln -sf /opt/bin/tcpdump /bin/tcpdump
busybox ln -sf /opt/bin/curl /bin/curl


# Aliaslar
alias grep='busybox-armv7l grep --color=auto'
alias ls='busybox-armv7l ls --color=auto'






