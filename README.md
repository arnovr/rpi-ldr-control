Raspberry PI - SqueezeBox Music control through LDR
===============
Install squeezelite:
http://www.raspberrypi.org/forums/viewtopic.php?f=38&t=23108

Edit squeeze the variables:
CURLURL and MAC.
CURLURL = corresponds with the ip adres of the squeezeserver, make sure the webclient is available
MAC = corresponds to the macadres in this file http://www.gerrelt.nl/RaspberryPi/squeezelite.sh , if you use it. 

Place squeeze in your bin directory, and the linux command "squeeze play" will start playing music on your RPi Squeeze player

Then i wanted to pickup the LDR input, and call the squeeze commands, so it actually starts and stops on the light.
That is where the ldr_control map is for, open the run.py in a text editor and change the following fields:
```
squeezecontrol = squeezebox.SqueezeControl('/bin/bash /usr/local/bin/', 10)
```
/usr/local/bin is the location i placed my squeeze file, if it is an other directory, alter it.
```
timingBorder = 1500
```
You may want to play around with the timing border ( < 1500 = lights on, > 1500 = lights off ), 1500 fits my needs.
IF you don't know the timings you hit, just add a print after 
```
timing = RCtime(gpio)
```
For example:
```
timing = RCtime(gpio)
print timing
```

```
gpio = 4
```
The GPIO pin you use on your raspberry. 



You might also want to change squeezebox/squeezecontact.py
I made a small time checker in it, so when you go to the bathroom late at night, you won't be scared by the music ;)
```
start = datetime.time(8, 0) // 8 AM
end = datetime.time(22, 30) // 10:30 PM

Thats it for settings, make the run.py script executable ( chmod +x run.py )
Add it to you'r startup script and you are all set!


Keep in mind, i did not put a massive effort in the code, it works, so i am content :p

![Hardware Setup](https://raw.githubusercontent.com/arnovr/rpi-ldr-control/master/images/DSCN2195.JPG "Hardware Setup")

![LDR](https://raw.githubusercontent.com/arnovr/rpi-ldr-control/master/images/DSCN2194.JPG "LDR")

