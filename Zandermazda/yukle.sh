adb shell mount -o remount,rw /system
adb push Web/ /online/custom_etc/zandermazda
adb shell "chmod -R 777 /online/custom_etc/zandermazda/"




busyboxx httpd -p 81 -h /online/custom_etc/zandermazda
