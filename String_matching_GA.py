'''
simple Genetic Algorithm for string matching and possible application for adaptive password cracking

Inspired by Zavia

by: Andy Zhou
Dec 28, 2018
'''

import random
from random import choice
import string
from fuzzywuzzy import fuzz
import numpy as np


class Agent:
    def __init__(self, length):
        #initializes an agent, which is a random string in a population to be evolved
        self.string = ''.join(choice(string.ascii_letters) for _ in range(length))
        self.fitness = -1





    def __str__(self):
        '''
        prints string
        '''

        return "Current String is {}, \t Fitness is: {}".format(str(self.string), str(self.fitness))




def stringGA(populationSize, stringlength):

    agents = initAgents(populationSize, stringlength)

    for generation in range(generations):
        #loop over each generation
        
        print('\nGeneration: ' + str(generation))

        agents = fitness(agents)    #compares agents with target string
        agents = selection(agents, stringlength)  #selects best agents for crossover
        agents = crossover(agents, stringlength)  #obtain offspring
        agents = mutation(agents, stringlength)   #mutate the offspring

        if any(agent.fitness >= 95 for agent in agents):
            print( 'Threshold met!')
            exit(0)



    


def initAgents(populationSize, length):
    '''

    :param populationSize: the number of random strings in the population
    :param length: length of each string
    :return: list of strings that have been initialized
    '''

    return [Agent(length) for _ in range(populationSize)]


def fitness(Agents):
    for agent in Agents:
        agent.fitness = fuzz.ratio(agent.string, target)

    return Agents


def selection(Agents, stringlength):
    agents = sorted(Agents, key = lambda Agent: Agent.fitness, reverse = True)
    print('\n'.join(map(str, agents)))

    agents = agents[:int(0.4*stringlength)]   #takes top 20% of agents with highest fitness values

    return agents

def crossover(Agents, stringlength):

    offspring = []
    for _ in range(int((populationSize - stringlength)/2)):
        parent1 = random.choice(Agents)
        parent2 = random.choice(Agents)

        child1 = Agent(stringlength)        #initialize child1 object
        child2 = Agent(stringlength)        #initiallize child2 object

        split = random.randint(0, stringlength)     #index upon which to split

        child1.string = parent1.string[0:split] + parent2.string[split:stringlength]
        child2.string = parent2.string[0:split] + parent1.string[split:stringlength]

        offspring.append(child1)
        offspring.append(child2)


    Agents.extend(offspring)

    return Agents


def mutation(Agents, stringlength):
    for agent in Agents:

        for idx, param in enumerate(agent.string):

            if random.betavariate(1, 1) <= 0.2:
                #mutate a random letter in position idx
                agent.string = agent.string[0:idx] + choice(string.ascii_letters) + agent.string[idx + 1:stringlength]

    return Agents


if __name__ == '__main__':
    populationSize = 40
    generations = 1000
    target = 'bigShaq'
    stringGA(populationSize, len(target))


