STDIN=$(cat -)

if [ "getdist" == "$STDIN"  ]; then

	 cat testfile.log | tail -n2 | head -n1 | cut -d"," -f 1

fi
if [ "getmotors" == "$STDIN"  ]; then

	 cat testfile.log | tail -n2 | head -n1 | cut -d"," -f 2

fi

if [ "start" == "$STDIN"  ]; then

	 python3 rigtig.py > testfile.log

fi
if [ "stop" == "$STDIN"  ]; then

	pkill -f "python3 rigtig.py"

fi
