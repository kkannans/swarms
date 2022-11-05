import pyrosim.pyrosim as pyrosim
import constants as c

def Create_World(id):
    pyrosim.Start_SDF("world"+str(id)+".sdf")
    pyrosim.Send_Cube(name="Box", pos=[2,2,0.5] , size=[1,1,1])
    pyrosim.End()

def Create_Body(self, torso_coordinates = None):
        pyrosim.Start_URDF("body"+str(self.agentID)+".urdf")
        torso_size = [1, 1, 1]
        frontLeg_size = [0.2, 1, 0.2]
        backLeg_size = frontLeg_size
        frontLowerLeg_size = [0.2, 0.2, 1]
        backLowerLeg_size = frontLowerLeg_size
        backLowerLeg_coordinates = [0, 0, -0.5*backLowerLeg_size[2]]
        frontLowerLeg_coordinates = [0, 0, -0.5*frontLowerLeg_size[2]]
        span_x = torso_size[0] + frontLeg_size[0] + backLeg_size[0]
        span_y = torso_size[1] + frontLeg_size[1] + backLeg_size[1]
        # generate starting coordinates for torso considering span in 2d plane
        delta = 1
        if torso_coordinates == None:
            torso_coordinates = [self.agentID*(span_x + delta), self.agentID*(span_y+delta), 1]
        # front and back legs
        # absolute
        joint_torso_backLeg_coordinates = [0 + torso_coordinates[0], -0.5*torso_size[1] + torso_coordinates[1], torso_size[2]]
        joint_torso_frontLeg_coordinates = [0 + torso_coordinates[0], 0.5*torso_size[1] + torso_coordinates[1], torso_size[2]]
        # rel to joint_torso_backLeg_coordinates
        backLeg_coordinates = [0 , -0.5*backLeg_size[1], 0]
        # rel to joint_torso_frontLeg_coordinates
        frontLeg_coordinates = [0, 0.5*frontLeg_size[1], 0]
        # rel to joint_torso_frontLeg_coordinates
        joint_frontLeg_frontLowerLeg_coordinates = [0, frontLeg_size[1], 0]
        # rel to joint_torso_backLeg_coordinates
        joint_backLeg_backLowerLeg_coordinates = [0, -1*backLeg_size[1], 0]
        pyrosim.Send_Cube(name="Torso", pos=torso_coordinates , size=torso_size) # absolute
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = joint_torso_backLeg_coordinates, jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=backLeg_coordinates , size=backLeg_size)
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = joint_torso_frontLeg_coordinates, jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=frontLeg_coordinates , size=frontLeg_size)
        pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = joint_frontLeg_frontLowerLeg_coordinates, jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=frontLowerLeg_coordinates , size=frontLowerLeg_size)
        pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = joint_backLeg_backLowerLeg_coordinates, jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=backLowerLeg_coordinates , size=backLowerLeg_size)

        # left and right legs
        rightLeg_size = [1, 0.2, 0.2]
        leftLeg_size = rightLeg_size
        leftLowerLeg_Size = [0.2, 0.2, 1]
        rightLowerLeg_Size = leftLowerLeg_Size
        # absolute
        joint_torso_leftLeg_coordinates = [-0.5*torso_size[0] + torso_coordinates[0], 0 + torso_coordinates[1], 1] 
        joint_torso_rightLeg_coordinates = [0.5*torso_size[0] + torso_coordinates[0], 0 + torso_coordinates[1], 1]
        # rel to joint_torso_leftLeg_coordinates
        leftLeg_coordinates = [-0.5*leftLeg_size[0], 0, 0]
        # rel to joint_torso_rightLeg_coordinates
        rightLeg_coordinates = [0.5*rightLeg_size[0], 0 ,0]
        # rel to joint_torso_leftLeg_coordinates
        joint_leftLeg_leftLowerLeg_coordinates = [-1*leftLeg_size[0], 0, 0]
        # rel to joint_torso_rightLeg_coordinates
        joint_rightLeg_rightLowerLeg_coordinates = [1*rightLeg_size[0], 0, 0]
        # rel to joint_leftLeg_leftLowerLeg_coordinates
        leftLowerLeg_coordinates = [0 , 0, -0.5*leftLowerLeg_Size[2]]
        # rel to joint_rightLeg_rightLowerLeg_coordinates
        rightLowerLeg_coordinates = [0, 0, -0.5*rightLowerLeg_Size[2]]
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = joint_torso_leftLeg_coordinates, jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=leftLeg_coordinates , size=leftLeg_size)
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = joint_torso_rightLeg_coordinates, jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=rightLeg_coordinates , size=rightLeg_size)
        pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = joint_leftLeg_leftLowerLeg_coordinates, jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=leftLowerLeg_coordinates , size=leftLowerLeg_Size)
        pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = joint_rightLeg_rightLowerLeg_coordinates, jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=rightLowerLeg_coordinates , size=rightLowerLeg_Size)
        pyrosim.End()


# For Quadraped
def Create_Body(id, numAgents):
    pyrosim.Start_URDF("body"+str(id)+".urdf")
    torso_size = [1, 1, 1]
    frontLeg_size = [0.2, 1, 0.2]
    backLeg_size = frontLeg_size
    frontLowerLeg_size = [0.2, 0.2, 1]
    backLowerLeg_size = frontLowerLeg_size
    backLowerLeg_coordinates = [0, 0, -0.5*backLowerLeg_size[2]]
    frontLowerLeg_coordinates = [0, 0, -0.5*frontLowerLeg_size[2]]
    # front and back legs
    # absolute
    torso_coordinates = [0, 0, 1]
    joint_torso_backLeg_coordinates = [0, -0.5*torso_size[1], torso_size[2]]
    joint_torso_frontLeg_coordinates = [0, 0.5*torso_size[1], torso_size[2]]
    # rel to joint_torso_backLeg_coordinates
    backLeg_coordinates = [0 , -0.5*backLeg_size[1], 0]
    # rel to joint_torso_frontLeg_coordinates
    frontLeg_coordinates = [0, 0.5*frontLeg_size[1], 0]
    # rel to joint_torso_frontLeg_coordinates
    joint_frontLeg_frontLowerLeg_coordinates = [0, frontLeg_size[1], 0]
    # rel to joint_torso_backLeg_coordinates
    joint_backLeg_backLowerLeg_coordinates = [0, -1*backLeg_size[1], 0]
    pyrosim.Send_Cube(name="Torso", pos=torso_coordinates , size=torso_size) # absolute
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = joint_torso_backLeg_coordinates, jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="BackLeg", pos=backLeg_coordinates , size=backLeg_size)
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = joint_torso_frontLeg_coordinates, jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="FrontLeg", pos=frontLeg_coordinates , size=frontLeg_size)
    pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = joint_frontLeg_frontLowerLeg_coordinates, jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="FrontLowerLeg", pos=frontLowerLeg_coordinates , size=frontLowerLeg_size)
    pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = joint_backLeg_backLowerLeg_coordinates, jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="BackLowerLeg", pos=backLowerLeg_coordinates , size=backLowerLeg_size)

    # left and right legs
    rightLeg_size = [1, 0.2, 0.2]
    leftLeg_size = rightLeg_size
    leftLowerLeg_Size = [0.2, 0.2, 1]
    rightLowerLeg_Size = leftLowerLeg_Size
    # absolute
    joint_torso_leftLeg_coordinates = [-0.5*torso_size[0], 0, 1]
    joint_torso_rightLeg_coordinates = [0.5*torso_coordinates[0],0, 1]
    # rel to joint_torso_leftLeg_coordinates
    leftLeg_coordinates = [-0.5*leftLeg_size[0], 0, 0]
    # rel to joint_torso_rightLeg_coordinates
    rightLeg_coordinates = [0.5*rightLeg_size[0], 0 ,0]
    # rel to joint_torso_leftLeg_coordinates
    joint_leftLeg_leftLowerLeg_coordinates = [-1*leftLeg_size[0], 0, 0]
    # rel to joint_torso_rightLeg_coordinates
    joint_rightLeg_rightLowerLeg_coordinates = [1*rightLeg_size[0], 0, 0]
    # rel to joint_leftLeg_leftLowerLeg_coordinates
    leftLowerLeg_coordinates = [0 , 0, -0.5*leftLowerLeg_Size[2]]
    # rel to joint_rightLeg_rightLowerLeg_coordinates
    rightLowerLeg_coordinates = [0, 0, -0.5*rightLowerLeg_Size[2]]
    pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = joint_torso_leftLeg_coordinates, jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="LeftLeg", pos=leftLeg_coordinates , size=leftLeg_size)
    pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = joint_torso_rightLeg_coordinates, jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="RightLeg", pos=rightLeg_coordinates , size=rightLeg_size)
    pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = joint_leftLeg_leftLowerLeg_coordinates, jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="LeftLowerLeg", pos=leftLowerLeg_coordinates , size=leftLowerLeg_Size)
    pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = joint_rightLeg_rightLowerLeg_coordinates, jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="RightLowerLeg", pos=rightLowerLeg_coordinates , size=rightLowerLeg_Size)
    pyrosim.End()


def Create_Brain(id, weights):
        pyrosim.Start_NeuralNetwork("brain"+str(id)+".nndf")
        # Sensor Neurons
        sensorNames = ["Field_Strength", "Field_Direction", "BackLowerLeg", "FrontLowerLeg", "RightLowerLeg","LeftLowerLeg"]
        assert c.numSensorNeurons <= len(sensorNames)
        for i in range(c.numSensorNeurons):
            pyrosim.Send_Sensor_Neuron(name = i , linkName = sensorNames[i])
        # Hidden neurons
        for i in range(c.numSensorNeurons, c.numSensorNeurons+c.numHiddenNeurons):
            pyrosim.Send_Hidden_Neuron(name = i)
        # Motor Neurons
        motorNeuronStart = c.numSensorNeurons+c.numHiddenNeurons
        jointNames = ["Torso_BackLeg", "Torso_FrontLeg", "Torso_RightLeg","Torso_LeftLeg",
                    "BackLeg_BackLowerLeg", "FrontLeg_FrontLowerLeg", "RightLeg_RightLowerLeg", "LeftLeg_LeftLowerLeg"]
        assert c.numMotorNeurons <= len(jointNames)
        for i in range(c.numMotorNeurons):
            pyrosim.Send_Motor_Neuron( name = i + motorNeuronStart , jointName = jointNames[i])
        # Synapses:
        start = 0
        for idx,layer in enumerate(weights):
            for currentRow in range(layer.shape[0]):
                for currentColumn in range(layer.shape[1]):
                    pyrosim.Send_Synapse(sourceNeuronName = currentRow + start, targetNeuronName = currentColumn+layer.shape[0], weight = layer[currentRow][currentColumn])
            start = (idx+1)*layer.shape[0]
        pyrosim.End()