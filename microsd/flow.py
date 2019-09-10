
class Flow(object):
	name='Flow'
	rate = 0.0

	def __init__(self, name=None, rate=0):
		self.name = name
		self.rate = rate

	### placeholder to recompute rate when needed
	def update_rate(self):
		return(self.rate)

	def step(self):
		return(self.rate)




class LinearEQFlow(Flow):
	dependencies = {}

	def update_rate(self):
		self.rate = sum([d.value * weight for d, weight in self.dependencies.items()])
		return(self.rate)

class ExponentialFlow(Flow):
	dependencies = {}

	def update_rate(self):
		self.rate = sum([d.value ** exponent for d, exponent in self.dependencies.items()])
		return(self.rate)