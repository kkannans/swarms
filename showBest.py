from glob import glob
from solution import SOLUTION
import numpy as np
import constants as c
import glob

bestBrainsFiles = glob.glob("bestBrain*.txt")
bestWeights = []
for fileName in bestBrainsFiles:
    bestWeights.append(np.loadtxt(fileName))

bestSolution = SOLUTION(0)
bestSolution.Set_Weights(bestWeights)
bestSolution.Start_Simulation("GUI")