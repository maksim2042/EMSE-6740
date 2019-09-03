import pandas as pd 

from stock import Stock
from flow import Flow, LinearEQFlow
from variable import Variable


### Simple bathtub model
bath = Stock(name='bathtub',upper_limit=100, lower_limit=0)
faucet = Flow(name='f_faucet',rate =1)
plug = Flow(name='f_plug', rate =0.5)

bath.in_flows.append(faucet)
bath.out_flows.append(plug)

evaporation = LinearEQFlow(name='evaporation', rate=0)
evaporation.dependencies = {bath:0.0011}
bath.out_flows.append(evaporation)

stocks= [bath]
flows = [faucet,plug,evaporation]


#def run():
result = pd.DataFrame()

while True:
	### Gather. data
	values = {s.name:s.value for s in stocks}

	flow_values = {f.name:f.rate for f in flows}
	values.update(flow_values)
	result = result.append(values,ignore_index=True)

	try:
		[f.update_rate() for f in flows]
		simulate = [s.step() for s in stocks]
	except Exception as e:
		### a thrown exception stops the run
		print str(e)
		print "simulation done"
		break

#	return result
	

