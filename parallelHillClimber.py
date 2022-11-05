from cmath import inf
from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np

class PARALLEL_HILL_CLIMBER:
    def __init__(self) -> None:
        self.parents = {}
        self.nextAvailableID = 0
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
    
    def evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            print("Generation = ", currentGeneration)
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Select()
        self.Print()
    
    def Evaluate(self, solutions):
        for solution in solutions.values():
            solution.Start_Simulation("DIRECT")
        for solution in solutions.values():
            solution.Wait_For_Simulation_To_End()

    def Print(self):
        for key in self.parents.keys():
            print("\n"+str(key)+": Parent fitness: "+str(self.parents[key].fitness)+", Child fitness: "+str(self.children[key].fitness)+"\n")

    def Spawn(self):
        self.children = {}
        for key in self.parents.keys():
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID+=1

    def Mutate(self):
        for child in self.children.values():
            child.mutate()

    def Select(self):
        for key in self.parents.keys():
            # if we are trying to maximize the negative x distance
            if (self.parents[key].fitness < self.children[key].fitness):
                self.parents[key] = self.children[key]

    def Show_Best(self):
        self.parents = sorted(self.parents.values(), key = lambda x: x.fitness, reverse = True)
        bestSolution = self.parents[0]
        print("Best fitness = ", self.parents[0].fitness)
        os.system("rm bestBrainLayer*.txt")
        bestWeights = bestSolution.weights
        for idx,weights in enumerate(bestWeights):
            weightsFileName = "bestBrainLayer"+str(idx)+".txt"
            weights = weights.reshape(weights.shape[0], -1)
            np.savetxt(weightsFileName, weights)
        self.parents[0].Start_Simulation("GUI")
        