#!/bin/sh

echo "Content-type: text/html; charset=utf-8"
echo

action=""
pid=""
args=""

# POST verisini oku
if [ "$REQUEST_METHOD" = "POST" ]; then
    read POST_DATA
    action=$(echo "$POST_DATA" | sed -n 's/.*action=\([^&]*\).*/\1/p' | sed 's/+/ /g; s/%3A/:/g; s/%2F/\//g')
    pid=$(echo "$POST_DATA" | sed -n 's/.*pid=\([^&]*\).*/\1/p')
    args=$(echo "$POST_DATA" | sed -n 's/.*args=\([^&]*\).*/\1/p' | sed 's/+/ /g; s/%3A/:/g; s/%2F/\//g')
fi

if [ "$action" = "kill" ] && [ -n "$pid" ]; then
    kill -9 "$pid" 2>/dev/null
elif [ "$action" = "restart" ] && [ -n "$pid" ] && [ -n "$args" ]; then
    kill -9 "$pid" 2>/dev/null
    nohup $args >/dev/null 2>&1 &
fi

cat <<EOF
<html>
<head>
    <title>Linux Modem Uygulamaları</title>
    <style>
        table { border-collapse: collapse; width: 80%; }
        th, td { border: 1px solid #ccc; padding: 8px; }
        th { background: #eee; }
        form { display: inline; }
    </style>
</head>
<body>
    <h2>Çalışan Uygulamalar</h2>
    <table>
        <tr>
            <th>PID</th>
            <th>Uygulama</th>
            <th>Komut Satırı</th>
            <th>İşlemler</th>
        </tr>
EOF

ps -eo pid,comm,args | tail -n +2 | while read pid comm args; do
    # Kernel thread'leri atla
    case "$comm" in
        \[*\]) continue ;;
    esac
    echo "<tr>"
    echo "<td>$pid</td>"
    echo "<td>$comm</td>"
    echo "<td>$args</td>"
    echo "<td>"
    # Kapat butonu
    echo "<form method=\"post\">"
    echo "<input type=\"hidden\" name=\"action\" value=\"kill\">"
    echo "<input type=\"hidden\" name=\"pid\" value=\"$pid\">"
    echo "<input type=\"submit\" value=\"Kapat\">"
    echo "</form>"
    # Yeniden başlat butonu
    echo "<form method=\"post\">"
    echo "<input type=\"hidden\" name=\"action\" value=\"restart\">"
    echo "<input type=\"hidden\" name=\"pid\" value=\"$pid\">"
    echo "<input type=\"hidden\" name=\"args\" value=\"$args\">"
    echo "<input type=\"submit\" value=\"Yeniden Başlat\">"
    echo "</form>"
    echo "</td>"
    echo "</tr>"
done

cat <<EOF
    </table>
</body>
</html>
EOF
