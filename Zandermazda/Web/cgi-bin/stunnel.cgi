#!/bin/sh
# CGI başlıklarını yazdır
echo "Content-Type: text/plain"
echo ""

# İstek tipini al
method=$REQUEST_METHOD

# Gelen isteği kontrol et
if [ "$method" = "GET" ]; then
    echo "Gelen istek tipi: GET"
elif [ "$method" = "POST" ]; then
    echo "Gelen istek tipi: POST"
elif [ "$method" = "PUT" ]; then
    echo "Gelen istek tipi: PUT"
elif [ "$method" = "DELETE" ]; then
    echo "Gelen istek tipi: DELETE"
else
    echo "Bilinmeyen istek tipi: $method"
fi


env
