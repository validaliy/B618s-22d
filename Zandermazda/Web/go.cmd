@title Cell ID Options  

@setlocal

@prompt $G 



@adb kill-server

adb connect 192.168.8.1:5555

adb shell mount -o remount,rw /system
adb push cgi-bin /system/zandermazda
adb push css/mystyle.css /system/zandermazda/css/mystyle.css
adb push js/myscript.js /system/zandermazda/js/myscript.js
adb push index.html /system/zandermazda
adb shell chmod 775 /system/zandermazda
adb shell chmod 775 /system/zandermazda/cgi-bin
adb shell chmod 664 /system/zandermazda/index.html
adb shell chmod 777 /system/zandermazda/cgi-bin/balong-nvtool
adb shell chmod 777 /system/zandermazda/cgi-bin/celllock.cgi
adb shell chmod 777 /system/zandermazda/cgi-bin/ayarlar.cgi
adb shell chmod 777 /system/zandermazda/cgi-bin/cellunlock.cgi
adb shell mount -o remount,ro /system

@echo Islem Bitti.

@pause > nul

@exit /B
