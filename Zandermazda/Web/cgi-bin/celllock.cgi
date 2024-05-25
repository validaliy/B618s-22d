#!/bin/sh
# Script Created by Zander Mazda

echo HTTP/1.1 301 Moved Permanently
echo Location: http://192.168.8.1/
echo Content-type: text/plain
echo
echo "$(date +%H:%M:%S) celllock.cgi" >> /tmp/sebeke.log

case "$REQUEST_METHOD" in
POST)
(
FILE=`cat`
BANDSX=`echo "$FILE" | busyboxx cut -f 1 -d '&' | busyboxx cut -f 2 -d '='`
PCIX=`echo "$FILE" | busyboxx cut -f 2 -d '&' | busyboxx cut -f 2 -d '='`
DLFREQX=`echo "$FILE" | busyboxx cut -f 3 -d '&' | busyboxx cut -f 2 -d '='`
BANDS=`busyboxx printf "%02x\n" $BANDSX | busyboxx awk '{print toupper($0)}'`
PCI1=`busyboxx printf "%04x\n" $PCIX | busyboxx awk '{print toupper($0)}' | busyboxx cut -c3,4`
PCI2=`busyboxx printf "%04x\n" $PCIX | busyboxx awk '{print toupper($0)}' | busyboxx cut -c1,2`
DLFREQ1=`busyboxx printf "%04x\n" $DLFREQX | busyboxx awk '{print toupper($0)}' | busyboxx cut -c3,4`
DLFREQ2=`busyboxx printf "%04x\n" $DLFREQX | busyboxx awk '{print toupper($0)}' | busyboxx cut -c1,2`
/system/zandermazda/cgi-bin/balong-nvtool -m 53810:03:00:00:00:$BANDS:01:$BANDS:01:$PCI1:$PCI2:$DLFREQ1:$DLFREQ2:00:00:00:00 > /dev/null 2>&1
reboot
)
;;
*)
esac