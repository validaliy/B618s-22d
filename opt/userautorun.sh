  GNU nano 7.2                                                  /opt/user-autorun.sh                                                             
#!/system/bin/busybox-armv7l sh
echo "user-autorun.sh icinden calisti" >> /tmp/kayitlar.log

echo "$(date +%H:%M:%S) shadowsocks basliyor" >> /tmp/kayitlar.log
sleep 5 && /online/ss-start.sh

echo "$(date +%H:%M:%S) stunnel basliyor" >> /tmp/kayitlar.log
sleep 2 && /opt/bin/stunnel


echo "$(date +%H:%M:%S) baslangic.sh basliyor" >> /tmp/kayitlar.log
source /opt/baslangic.sh

echo "$(date +%H:%M:%S) user-autorun.sh bitti" >> /tmp/kayitlar.log


#sleep 60 && /patch/to/prog &> /dev/null &





