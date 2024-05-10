



#.....................

busybox ln -sf /system/bin/busybox-armv7l /bin/wget
busybox ln -sf /system/bin/busybox-armv7l /bin/gzip

ln -s /online/opt /opt
#User's autorun
/online/opt/user-autorun.sh
