#!/bin/sh
echo "Content-type: text/html; charset=UTF-8"
echo ""

echo "<html><head><title>CGI Information</title></head><body>"
echo "<h1>CGI Bilgileri</h1>"

# Kullanıcı bilgilerini göster
echo "<h2>Kullanıcı Bilgileri</h2>"
echo "<p>IP Adresi: $REMOTE_ADDR</p>"
echo "<p>Tarayıcı Bilgisi: $HTTP_USER_AGENT</p>"
echo "<p>İstek Metodu: $REQUEST_METHOD</p>"
echo "<p>Sorgu Stringi: $QUERY_STRING</p>"

# Server bilgilerini göster
echo "<h2>Sunucu Bilgileri</h2>"
echo "<p>Sunucu Yazılımı: $SERVER_SOFTWARE</p>"
echo "<p>Sunucu Adı: $SERVER_NAME</p>"
echo "<p>Sunucu Protokolü: $SERVER_PROTOCOL</p>"
echo "<p>Gateway Interface: $GATEWAY_INTERFACE</p>"
echo "<p>CGI Betik Yolu: $SCRIPT_NAME</p>"

echo "<h2>Ortam Değişkenleri</h2>"
echo "<ul>"
for var in $(printenv); do
    echo "<li>$var</li>"
done
echo "</ul>"

echo "</body></html>"