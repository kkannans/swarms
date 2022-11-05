from cmath import phase
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
import time
import sys
import constants as c
from simulation import SIMULATION

if len(sys.argv) > 2:
    directOrGUI = sys.argv[1]
    solutionID = sys.argv[2]
elif len(sys.argv) == 2:
    directOrGUI = "GUI"
    solutionID = sys.argv[1]
# pybullet simulation init
simulation = SIMULATION(c.simSteps, directOrGUI, solutionID)
simulation.Run(c.sleepTime)
simulation.Get_Fitness()


