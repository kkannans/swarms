import numpy as np
import pyrosim.pyrosim as pyrosim
import os

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.linkID = pyrosim.linkNamesToIndices[self.linkName]
        self.values = None

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Set_Value(self, t, value):
        self.values[t] = value

    def Save_Commands(self):
        path = "data/"+str(self.linkName)+"_sensor.npy"
        if not os.path.exists(os.path.join(os.getcwd()+"/data")):
            os.makedirs(os.path.join(os.getcwd()+"/data"))
        np.save(path, self.values)

    def __del__(self):
        # self.Save_Commands()
        pass