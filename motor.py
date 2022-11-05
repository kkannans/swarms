import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c
from trajectory import *
import numpy as np
class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

    def Set_Value(self, desiredValue, robotID):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotID, 
                    jointName = self.jointName, controlMode = p.POSITION_CONTROL,
                    targetPosition = desiredValue, maxForce = c.maxMotorForce)
    
    def __del__(self):
        return