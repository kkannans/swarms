import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import creation
import constants as c
import time 

class SOLUTION:
    def __init__(self, solutionID) -> None:
        self.myID = solutionID
        if c.numHiddenNeurons > 0:
            self.weights = [np.random.rand(c.numSensorNeurons,c.numHiddenNeurons), np.random.rand(c.numHiddenNeurons,c.numMotorNeurons)]
        else:
            self.weights = [np.random.rand(c.numSensorNeurons,c.numMotorNeurons)]
        self.weights = [2*weights - 1 for weights in self.weights]
    
    def Set_Weights(self, weights):
        self.weights = weights

    def Set_ID(self, id):
        self.myID = id

    def Start_Simulation(self, mode):
        creation.Create_World(self.myID)
        creation.Create_Body(self.myID, c.numAgents)
        creation.Create_Brain(self.myID, self.weights)
        command = "python3 simulate.py " + mode + " "+str(self.myID) + " 2&>1 &"
        # command = "python3 simulate.py " + mode + " "+str(self.myID)
        os.system(command)

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness"+str(self.myID)+".txt" 
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f = open(fitnessFileName, "r")
        self.fitness = float(f.read())
        f.close()
        # Delete the file after reading value
        os.system("rm "+fitnessFileName)


    def Evaluate(self, mode):
        self.Start_Simulation(mode)
        self.Wait_For_Simulation_To_End()

    def mutate(self):
        for weights in self.weights:
            randomRow = np.random.randint(0,weights.shape[0])
            randomColumn = np.random.randint(0,weights.shape[1])
            weights[randomRow][randomColumn] = np.random.random() * 2 - 1
