



#....................

echo "$(date +%H:%M:%S) kisa yollar tanimlaniyor..." > /tmp/kayitlar.log
busybox ln -sf /system/bin/busybox-armv7l /bin/wget
busybox ln -sf /system/bin/busybox-armv7l /bin/gzip
ln -s /online/opt /opt



#User's autorun
echo "$(date +%H:%M:%S) user-autorun.sh basliyor..." > /tmp/kayitlar.log
/online/opt/user-autorun.sh



echo "$(date +%H:%M:%S) AdguardHome Basliyor..." >> /tmp/kayitlar.log
#/online/AdGuardHome/AdGuardHome


echo "Bilgiler" >> /tmp/kayitlar.log
echo "$(ll /app/bin/dns) DNS" >> /tmp/kayitlar.log
echo "$(date +%H:%M:%S) Bu satira gecildiyse AdGuardHome Calismiyor." >> /tmp/kayitlar.log
