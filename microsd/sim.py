import pandas as pd 
import matplotlib.pyplot as plot

from stock import Stock
from flow import Flow, LinearEQFlow, ExponentialFlow
from variable import Variable
from random import shuffle


### PREDATOR AND PREY MODEL
sheep = Stock(name='sheep',lower_limit=0)
sheep.value=10


wolves = Stock(name='wolves')
wolves.value=20
wolves_birth_rate = LinearEQFlow(name='wolf_birth_rate',rate =0)
wolves_birth_rate.dependencies = {wolves:2}


grass = Stock(name ='grass')
grass.value=50
grass_growth_rate = Flow(name='grass_growth_rate',rate=100)
grass_eat_rate = LinearEQFlow(name='grass_eat_rate')
grass_eat_rate.dependencies={sheep:1}
grass.in_flows.append(grass_growth_rate)
grass.out_flows.append(grass_eat_rate)

birth = LinearEQFlow(name='birth_rate',rate =0)
birth.dependencies = {sheep:0.5}

death = LinearEQFlow(name='death',rate=0)
death.dependencies={sheep:0.07}

death_of_hunger = ExponentialFlow(name='death_of_hunger',rate=0)
death_of_hunger.dependencies={grass:-1}

sheep.in_flows.append(birth)
sheep.out_flows.append(death)
sheep.out_flows.append(death_of_hunger)


wolves = Stock(name='wolves')
wolves.value=20
wolves_birth_rate = LinearEQFlow(name='wolf_birth_rate',rate =0)
wolves_birth_rate.dependencies = {wolves:2}

wolf_death = LinearEQFlow(name='wolf_death',rate=0)
wolf_death.dependencies={wolves:0.07}

wolf_death_of_hunger = ExponentialFlow(name='wolf_death_of_hunger',rate=0)
wolf_death_of_hunger.dependencies={sheep:-1}

wolves.in_flows.append(wolves_birth_rate)
wolves.out_flows.append(wolf_death)
wolves.out_flows.append(wolf_death_of_hunger)

sheep_eaten = LinearEQFlow(name='sheep_eaten',rate=0)
sheep_eaten.dependencies = {wolves:0.25}
sheep.out_flows.append(sheep_eaten)



stocks= [sheep,grass,wolves]
flows = [birth,death,grass_eat_rate, sheep_eaten, grass_growth_rate,death_of_hunger,wolves_birth_rate,wolf_death_of_hunger,wolf_death]

#def run():
result = pd.DataFrame()


def step():
	### Gather. data
	global result
	values = {s.name:s.value for s in stocks}
	flow_values = {f.name:f.rate for f in flows}
	values.update(flow_values)
	result = result.append(values,ignore_index=True)

	try:
		shuffle(flows)
		shuffle(stocks)
		[f.update_rate() for f in flows]
		simulate = [s.step() for s in stocks]
	except Exception as e:
		### a thrown exception stops the run
		print str(e)
		print "simulation done"

#	return result
	
#while True:
for _ in range(100):
	step()
