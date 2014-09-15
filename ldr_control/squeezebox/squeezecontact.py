import datetime
class SqueezeContact:
	def mayContact(self):   
		start = datetime.time(8, 0)
		end = datetime.time(22, 30)
		now = datetime.datetime.now().time()
		if start < now < end:
			return True

		return False