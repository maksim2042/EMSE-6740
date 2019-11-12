from mesa import Agent, Model
from mesa.time import RandomActivation
from random import random, randint,choice
import pandas as pd


class FoxNews(Agent):
    def __init__(self, unique_id, g, model):
        super().__init__(unique_id, model)
        self.opinion = 0
        self.g = g
        self.neighbors = [] 

    def step(self):
        pass


class Bernie(Agent):
    def __init__(self, unique_id, g, model):
        super().__init__(unique_id, model)
        self.opinion = 1
        self.g = g
        self.neighbors = [] 

    def step(self):
        pass


class FAgent(Agent):
    """An agent with fixed initial wealth."""
    def __init__(self, unique_id, g, model):
        super().__init__(unique_id, model)
        self.opinion = random()-0.5 if random()>0.5 else random()+0.5
        self.g = g
        self.neighbors = [] 


    def step(self):
        if len(self.neighbors) == 0: return

        friends_opnion = sum([(1-(self.opinion-f.opinion))*f.opinion for f in self.neighbors]) / float(len(self.neighbors))
        self.opinion = (1-self.g)*self.opinion + self.g*friends_opnion



class FriedkinModel(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.alpha=0.3
        self.i = 1
        self.num_agents = N
        # Create agents
        self.schedule = RandomActivation(self)
        # Create agents

        fox = FoxNews(-1, 0, self)
        bernie = Bernie(-2, 0, self)
        self.schedule.add(fox)
        self.schedule.add(bernie)

        for i in range(self.num_agents):
            exp = 0.7
            a = FAgent(i, exp, self)
            self.schedule.add(a)

        for a in self.schedule.agents:
            a.neighbors = [aa for aa in self.schedule.agents if random() < self.alpha]
            a.neighbors.append(fox if random()>0.5 else bernie)




    def step(self):
        '''Advance the model by one step.'''
        global agent_opinion
        self.i+=1
        self.schedule.step()
        agent_opinion = agent_opinion.append(
            pd.DataFrame([{'step':self.i, 'id':a.unique_id, 'o':a.opinion} for a in model.schedule.agents]))


agent_opinion = pd.DataFrame()

model = FriedkinModel(100)
for i in range(20):
    if i % 100 ==0: print(i)
    model.step()


