import squeezebox
import RPi.GPIO as GPIO, time
import os


squeezecontrol = squeezebox.SqueezeControl('/bin/bash /usr/local/bin/', 10)
squeezecontact = squeezebox.SqueezeContact()

out = ''
timing = 0
gpio = 4
playing = 0
playhits = 0
stophits = 0
timingBorder = 1500
mustHitTimes = 5

maxHitTimeshits = 0 #counter van maximale measurement hits
maxHitTimes = 2 #maximale hits van maximimae measurement
maxTimingBorder = 10000 # maximale measurement
extraSleeper = 2 # aantal seconden slapen als maximale measurement geraakt

# Tell the GPIO library to use
# Broadcom GPIO references
GPIO.setmode(GPIO.BCM)


def RCtime (PiPin):
	measurement = 0
	# Discharge capacitor
	GPIO.setup(PiPin, GPIO.OUT)
	GPIO.output(PiPin, GPIO.LOW)
	time.sleep(0.1)

	GPIO.setup(PiPin, GPIO.IN)
	# Count loops until voltage across
	# capacitor reads high on GPIO
	while (GPIO.input(PiPin) == GPIO.LOW):
		if measurement < maxTimingBorder:
			measurement += 1
		else:
			break

	return measurement

while True:
	if squeezecontact.mayContact() == True:
		timing = RCtime(gpio)

		if timing == maxTimingBorder:
			maxHitTimeshits = maxHitTimeshits + 1
			if maxHitTimeshits == maxHitTimes:
				time.sleep(extraSleeper) #extra vertraging, anders zuigt hij cpu
				maxHitTimeshits = 0
		

		if timing <= timingBorder:
			if playing == 0:
				playhits = playhits + 1
				if stophits >= 1:
					stophits = stophits - 1

				if playhits > mustHitTimes:
					squeezecontrol.play()
					playing = 1
		else:
			if playing == 1:
				stophits = stophits + 1
				if playhits >= 1:
					playhits = playhits - 1

				if stophits > mustHitTimes:
					squeezecontrol.pause()
					playing = 0
	else:
		time.sleep(600) #sleep 10 minutes, before checking again