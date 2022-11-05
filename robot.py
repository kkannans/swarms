from mimetypes import MimeTypes
import pybullet as p
from pyrosim.neuron import NEURON
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import constants as c
import numpy as np
import os
from trajectory import Compute_Sinusoidal_Trajectory
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self, simTime, solutionID):
        self.solutionID = solutionID
        bodyFileName = "body"+str(self.solutionID)+".urdf"
        brainFileName = "brain"+str(self.solutionID)+".nndf"
        self.robotID = p.loadURDF(bodyFileName)
        self.nn = NEURAL_NETWORK(brainFileName)
        os.system("rm "+brainFileName)
        os.system("rm "+bodyFileName)
        pyrosim.Prepare_To_Simulate(self.robotID)
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
        self.Prepare_To_Sense(simTime)
    
    def Prepare_To_Sense(self, simTime):
        self.sensors = {}
        for linkName,index in pyrosim.linkNamesToIndices.items():
            self.sensors[index] = SENSOR(linkName)
            self.sensors[index].values = np.zeros(simTime)

    def Sense(self, t):
        for sensorID, sensor in self.sensors.items():
            sensor.Get_Value(t)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = c.motorJointRange*self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(desiredAngle, self.robotID)

    def Think(self, t):
        # Update with sensors[linkNamestoIndices] and time step
        self.nn.Update(self.sensors, t)
        # self.nn.Print()

    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotID)
        basePosition = basePositionAndOrientation[0]
        fitness_to_track = -1*basePosition[0]
        tmpFileName = "tmp"+str(self.solutionID)+".txt"
        f = open(tmpFileName, "w")
        f.write(str(fitness_to_track))
        f.close()
        fitnessFileName = "fitness"+str(self.solutionID)+".txt"
        # move to fitnessID.txt
        moveCommand = "mv "+tmpFileName+" "+fitnessFileName
        os.system(moveCommand)
        





