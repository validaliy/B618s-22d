#!/bin/sh

echo "Content-type: text/html; charset=UTF-8"
echo
echo "$(date +%H:%M:%S) komut.cgi" >> /tmp/sebeke.log

cat <<EOF
<html><head>
<meta charset="utf-8">
<title>B618s-22d</title>
</head> <body>
<h3>Log</h3>
<p>$(date)</p>
EOF

case "$REQUEST_METHOD" in
POST)
(
echo "$QUERY_STRING"
)
;;
*)
esac

echo "</body></html>"