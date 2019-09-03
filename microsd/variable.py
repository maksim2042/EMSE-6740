
def Variable(object):
	value =0.0
	name = 'Var'

	def __init__(name=None, value = 0.0):
		self.name=name
		self.value = value

	def update_value(self):
		return(self.rate)