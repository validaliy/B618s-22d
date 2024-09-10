#!/bin/sh
echo "Content-type: text/html; charset=UTF-8"
echo ""

echo "<html><head><title>CGI Information</title></head><body>"
echo "<h1>Directory Listing</h1>"
echo "<ul>"

for file in $(ls); do
    echo "<li><a href=\"$file\">$file</a></li>"
done

echo "</ul>"
echo "</body></html>"