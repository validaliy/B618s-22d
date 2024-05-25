#!/bin/sh


# echo HTTP/1.1 301 Moved Permanently
# echo Location: http://192.168.8.1/
echo Content-type: text/html
echo
echo '<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"><link rel="stylesheet" href="../css/mystyle.css"><title>İbrahim Beylem</title></head>'
echo "<body>"
echo "merhaba <br>"
echo "saat $(date +%H:%M:%S) <br>"

echo "<pre class='code'>şimdi:<br>$(atc at^lcellinfo=0 | grep LCELLINFO) <br>"
echo "Kullanılabilir:<br>$(atc at^lcellinfo=1 | grep LCELLINFO) <br>"

if [[ $(ls -l /app/bin/dns) == *"rwxrwxrwx"* ]]; then
  echo "Dns: Vodafone"
else
  echo "Dns Yok ???"
fi

echo "<br> Kayıtlar.log: <br> $(cat /tmp/kayitlar.log)"
echo "</pre>"

echo "<table><tr><th>baslik</th><th>Cevap</th> </tr>"
echo "<tr><td>SERVER_SOFTWARE:</td><td>$SERVER_SOFTWARE </td></tr>"
echo "<tr><td>SERVER_NAME:</td><td>$SERVER_NAME </td></tr>"
echo "<tr><td>GATEWAY_INTERFACE:</td><td>$GATEWAY_INTERFACE </td></tr>"
echo "<tr><td>SERVER_PROTOCOL:</td><td>$SERVER_PROTOCOL </td></tr>"
echo "<tr><td>SERVER_PORT:</td><td>$SERVER_PORT </td></tr>"
echo "<tr><td>REQUEST_METHOD:</td><td>$REQUEST_METHOD </td></tr>"
echo "<tr><td>PATH_INFO</td><td>$PATH_INFO </td></tr>"
echo "<tr><td>PATH_TRANSLATED:</td><td>$PATH_TRANSLATED </td></tr>"
echo "<tr><td>SCRIPT_NAME:</td><td>$SCRIPT_NAME </td></tr>"
echo "<tr><td>QUERY_STRING:</td><td>$QUERY_STRING </td></tr>"
echo "<tr><td>REMOTE_HOST:</td><td>$REMOTE_HOST </td></tr>"
echo "<tr><td>REMOTE_ADDR:</td><td>$REMOTE_ADDR </td></tr>"
echo "<tr><td>AUTH_TYPE:</td><td>$AUTH_TYPE </td></tr>"
echo "<tr><td>REMOTE_USER:</td><td>$REMOTE_USER </td></tr>"
echo "<tr><td>CONTENT_TYPE:</td><td>$CONTENT_TYPE </td></tr>"
echo "<tr><td>CONTENT_LENGTH:</td><td>$CONTENT_LENGTH </td></tr>"
echo "<tr><td>HTTP_ACCEPT:</td><td>$HTTP_ACCEPT </td></tr>"
echo "<tr><td>HTTP_USER_AGENT:</td><td>$HTTP_USER_AGENT </td></tr>"
# echo <tr>XXXXXXXXX: $XXXXXXXXX</tr>
echo "</table>"
echo "$(date +%H:%M:%S) ayarlar.cgi" >> /tmp/sebeke.log
echo "</body></html>"

case "$REQUEST_METHOD" in
POST)
(
  echo "$(date +%H:%M:%S) ayarlar.cgi yeniden baslatiliyor..." >> /tmp/sebeke.log
  echo "$POST"
  reboot

)
;;
*)
esac

