@echo off
cls
plink -ssh pi@raspberrypi -pw Raspberry0 -batch "sudo killall python"
pscp -l pi -pw Raspberry0 src/*.py pi@raspberrypi:/home/pi/python/&&cls&&plink -ssh pi@raspberrypi -pw Raspberry0 -batch "cd /home/pi/python/&&sudo python index.py"
