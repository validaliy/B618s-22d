#!/bin/sh

STUNNELFILE="stunnel.conf"

echo "Content-Type: text/plain"
echo ""

# İstek tipini al
method=$REQUEST_METHOD

# Gelen isteği kontrol et
if [ "$method" = "GET" ]; then
    echo "Gelen istek tipi: GET"
    if [ -f "$STUNNELFILE" ]; then
        # Dosya içeriğini oku ve HTML özel karakterlerini kaçışla
        content=$(cat "$STUNNELFILE" | sed 's/&/\&amp;/g; s/</\&lt;/g; s/>/\&gt;/g; s/"/\&quot;/g; s/'"'"'/\&#39;/g')
        echo "<p>$content</p>"
    else
        echo "<p>File not found: $STUNNELFILE</p>"
    fi
elif [ "$method" = "POST" ]; then
    echo "Gelen istek tipi: POST"
    # sni anahtarının değerini al
    sni_value=$(echo "$QUERY_STRING" | awk -F'&' '{for(i=1;i<=NF;i++){if($i ~ /^sni=/){print $i}}}' | sed 's/sni=//')
    echo "SNI Değeri: $sni_value"

        # stunnel.conf dosyasındaki sni değerini güncelle
    if [ -f "$STUNNELFILE" ]; then
        sed -i "s/^sni = .*/sni = $sni_value/" "$STUNNELFILE"
        echo "stunnel.conf dosyasındaki sni değeri güncellendi."
    else
        echo "File not found: $STUNNELFILE"
    fi
else
    echo "Bilinmeyen istek tipi: $method"
fi