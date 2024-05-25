#!/bin/sh
# Script Created by Zander Mazda

# echo "HTTP/1.1 301 Moved Permanently"
# echo Location: http://192.168.8.1/
echo "Content-type: text/html"
echo "cellunlock" > /tmp/sebeke.log
echo "$(date +%H:%M:%S) celllock.cgi" >> /tmp/sebeke.log

case "$REQUEST_METHOD" in
POST)
(
/system/zandermazda/cgi-bin/balong-nvtool -m 53810:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00 > /dev/null 2>&1
reboot
)
;;
*)
esac