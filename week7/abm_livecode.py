from mesa import Agent, Model
from mesa.time import RandomActivation
from random import random, randint

class MoneyAgent(Agent):
    """An agent with fixed initial wealth."""
    def __init__(self, unique_id, wages, exp, model):
        super().__init__(unique_id, model)
        self.wealth = 1.0
        self.wages = wages
        self.exp=exp

    def step(self):
        # The agent's step will go here.
        other_agent = self.random.choice(self.model.schedule.agents)

        ### apply a simple production function
        income = self.wages**(1-self.exp) + self.wealth**self.exp
        self.wealth = self.wealth+income

        if other_agent.wealth ==0: 
            return
        else:
            other_agent.wealth -= 1
            self.wealth += 1

class MoneyModel(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.num_agents = N
        # Create agents
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            wages = float(randint(1,10))
            exp = random()/2
            a = MoneyAgent(i, wages, exp, self)
            self.schedule.add(a)

    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()

model = MoneyModel(100)
for i in range(1000):
    if i % 100 ==0: print(i)
    model.step()

import pandas as pd
agent_wealth = pd.DataFrame([{'id':a.unique_id, 'w':a.wealth} for a in model.schedule.agents])