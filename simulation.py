from pytest import Session
from world import WORLD
from robot import ROBOT
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import os
import numpy as np
import time

class SIMULATION:
    def __init__(self, simSteps, directOrGUI, solutionID):
        self.mode = directOrGUI
        self.solutionID = solutionID
        if self.mode == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        self.simSteps = simSteps
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        p.resetDebugVisualizerCamera( cameraDistance=15, cameraYaw=60, cameraPitch=-20, cameraTargetPosition=[0,0,0])
        self.world = WORLD(self.solutionID)
        self.robot = ROBOT(self.simSteps, self.solutionID)

    def Run(self, sleepTime):
        for t in range(self.simSteps):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think(t)
            self.robot.Act(t)
            if self.mode == "GUI":
                time.sleep(sleepTime)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()
