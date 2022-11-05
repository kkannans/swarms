import pybullet as p
import os
class WORLD:
    def __init__(self, solutionID):
        self.planeId = p.loadURDF("plane.urdf")
        self.worldFilePath = "world"+str(solutionID)+".sdf"
        p.loadSDF(self.worldFilePath)

    def __del__(self):
        os.system("rm "+self.worldFilePath)