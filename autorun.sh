



#....................

echo "$(date +"%d.%m.%Y %H:%M"): kisa yollar tanimlaniyor..." > /tmp/kayitlar.log
busybox ln -sf /system/bin/busybox-armv7l /bin/wget
busybox ln -sf /system/bin/busybox-armv7l /bin/gzip
ln -s /online/opt /opt



#User's autorun
echo "$(date +"%d.%m.%Y %H:%M"): user-autorun.sh basliyor..." > /tmp/kayitlar.log
/online/opt/user-autorun.sh


#kisayollar
source /opt/baslangic.sh


#echo "$(date +"%d.%m.%Y %H:%M"): AdguardHome Basliyor..." >> /tmp/kayitlar.log
#/online/AdGuardHome/AdGuardHome


echo "Bilgiler" >> /tmp/kayitlar.log
echo "$(ll /app/bin/dns) DNS" >> /tmp/kayitlar.log
echo "$(date +"%d.%m.%Y %H:%M"): Bu satira gecildiyse AdGuardHome Calismiyor." >> /tmp/kayitlar.log 

