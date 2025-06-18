@title Cell ID Options  

REM busyboxx httpd -p 81 -h /online/custom_etc/zandermazda

@setlocal

@prompt $G 



@adb kill-server

adb connect 10.147.18.11:5555

adb shell mount -o remount,rw /system
adb push Web /online/custom_etc/zandermazda
adb shell mount -o remount,ro /system

@echo Islem Bitti.

@pause > nul

@exit /B
