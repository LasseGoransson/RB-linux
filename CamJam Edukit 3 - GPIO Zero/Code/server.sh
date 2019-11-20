STDIN=$(cat -)

if [ "getdist" == "$STDIN"  ]; then

	 cat testfile.log | tail -n2 | head -n1 | cut -d"," -f 1

fi
if [ "getmotors" == "$STDIN"  ]; then

	 cat testfile.log | tail -n2 | head -n1 | cut -d"," -f 2

fi

if [ "start" == "$STDIN"  ]; then

	sudo pigpiod && GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=localhost python3 rigtig.py > testfile.log

fi
if [ "stop" == "$STDIN"  ]; then

	pkill -f "python3 rigtig.py"
	sudo killall "pigpiod"
	gpio write 11 0
	gpio write 13 0

fi
