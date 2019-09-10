from flow import Flow 

class Stock(object):
	name = "Test"
	value = 0.0
	in_flows = []
	out_flows = []

	upper_limit = 100
	lower_limit = 0

	def __init__(self, name='Test', value=0.0, upper_limit=float('inf'), lower_limit=-float('inf')):
		self.name = name
		self.value = value
		self.upper_limit=upper_limit
		self.lower_limit = lower_limit



	def step(self):
		total_inflow = sum([inf.step() for inf in self.in_flows])
		total_outflow = sum([outf.step() for outf in self.out_flows])

		self.value = self.value + total_inflow - total_outflow

		if self.value > self.upper_limit:
			raise(Exception("Upper limit reached for %s. Value %s > %s "%(self.name, self.value, self.upper_limit)))

		if self.value > self.upper_limit:
			raise(Exception("Lower limit reached for %s. Value %s < %s "%(self.name, self.value, self.lower_limit)))

		return self.value