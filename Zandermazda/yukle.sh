adb shell mount -o remount,rw /system
adb push Web/ /system/zandermazda
adb shell "chmod 777 /system/zandermazda/*"




busyboxx httpd -p 81 -h /system/zandermazda/