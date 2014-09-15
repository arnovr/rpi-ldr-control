import os, time
import subprocess as sub

class SqueezeControl:
	timeOut = 10
	startscript = ''

	def __init__(self, startscript, timeout):
		self.startscript
		self.timeOut = timeout

  	def stop(self):
  		print 'Pause squeezebox'
  		os.system('squeeze pause')
		time.sleep(self.timeOut)
		
	def pause(self):
		print 'Pause squeezebox'
		if self.isPlaying() == True:
			os.system(self.startscript + 'squeeze pause')

		time.sleep(self.timeOut)

	def play(self):
		print 'Start squeezebox'
		os.system(self.startscript + 'squeeze play')
		time.sleep(self.timeOut)

	def isPlaying(self):
		print 'squeezebox isPlaying'
		f = os.popen(self.startscript + 'squeeze isPlaying')
		output = f.read()
		if "1" in output:
			return True
		else:
			return False

	def poweroff(self):
		print 'Poweroff squeezebox'
		os.system(self.startscript + 'squeeze poweroff');
		time.sleep(self.timeOut)

	def poweron(self):
		print 'Poweron squeezebox'
		os.system(self.startscript + 'squeeze poweron');
		time.sleep(self.timeOut)