from mesa import Agent, Model
from mesa.time import RandomActivation
from random import random, randint,choice


class Firm(Agent):
    def __init__(self,unique_id, alpha,model):
        super().__init__(unique_id, model)
        self.agents = []
        self.utility=0
        self.alpha = random()
        self.beta = 1-alpha
        self.dead=False

    def step(self):
        effort = sum([a.effort for a in self.agents])
        self.utility = self.alpha * effort + self.beta * effort**2 
        if len(self.agents) == 0:
            self.dead = True
        else:
            self.income = self.utility/float(len(self.agents))

class FirmAgent(Agent):
    """An agent with fixed initial wealth."""
    def __init__(self, unique_id, exp, model):
        super().__init__(unique_id, model)
        self.utility = 0
        self.effort = 1
        self.exp=exp
        self.job = None

    def step(self):
        # The agent's step will go here.
        if not self.job:
            self.job = Firm(0-self.unique_id,1,self.model)
            self.job.agents.append(self)
            self.model.schedule.add(self.job)

        self.effort =self.exp
        self.utility = (self.job.utility**self.exp) * ((1-self.effort)**(1-self.exp))

        ### am I happy?
        doo = choice(['stay','leave','startup'])
        if doo =='leave':
            ### join a random firm
            firms = [f for f in model.schedule.agents if isinstance(f,Firm) and not f.dead]
            self.job.agents.remove(self)  ### quit my job
            self.job = choice(firms) ### find a new job
            self.job.agents.append(self) ##$ add mysefl to payroll
        elif doo == 'startup':
            self.job = Firm(1000-self.unique_id,1,self.model)
            self.job.agents.append(self)
            self.model.schedule.add(self.job)  



class FirmModel(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.alpha=0.5
        self.beta = 1-self.alpha
        self.num_agents = N
        # Create agents
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            exp = random()
            a = FirmAgent(i, exp, self)
            self.schedule.add(a)

    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()



model = FirmModel(100)
for i in range(1000):
    if i % 100 ==0: print(i)
    model.step()

import pandas as pd
agent_wealth = pd.DataFrame([{'id':a.unique_id, 'w':a.utility} for a in model.schedule.agents])
firms = [f for f in model.schedule.agents if isinstance(f,Firm)]
firm_wealth = pd.DataFrame([{'id':f.unique_id, 'size':len(f.agents),'w':f.utility} for f in firms])

