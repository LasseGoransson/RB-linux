cd /home/pi/here/
socat tcp-listen:8080,reuseaddr,fork exec:'bash "server.sh"'
