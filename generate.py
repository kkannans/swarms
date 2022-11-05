from os import link
from random import random
import numpy as np
from turtle import back
import pyrosim.pyrosim as pyrosim

def Create_World():
	pyrosim.Start_SDF("world.sdf")
	pyrosim.Send_Cube(name="Box", pos=[2,2,0.5] , size=[1,1,1])
	pyrosim.End()

def compute_joint_coordinates(parent, child):
	joint_coordinates = [(parent[0] - child[0])/2,
						(parent[1] - child[1])/2,
						(parent[2] - child[2])/2]
	return joint_coordinates

# Generate Body for quadraped
def Generate_Body():
	link_size = [1, 1, 1]
	torso_coordinates = [1,0, 1.5*link_size[2]]
	pyrosim.Start_URDF("body.urdf")
	joint_torso_backleg_coordinates = [torso_coordinates[0]-0.5, 0, torso_coordinates[2]-(0.5*link_size[2])]
	backLeg_coordinates = [link_size[0]*(-0.5),0,link_size[2]*(-0.5)]
	joint_torso_frontleg_coordinates = [torso_coordinates[0]+0.5, 0, torso_coordinates[2]-(0.5*link_size[2])]
	frontLeg_coordinates = [link_size[0]*0.5,0,link_size[2]*(-0.5)]
	pyrosim.Send_Cube(name="Torso", pos=torso_coordinates , size=link_size) # absolute
	pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = joint_torso_backleg_coordinates)
	pyrosim.Send_Cube(name="BackLeg", pos=backLeg_coordinates , size=link_size)
	pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = joint_torso_frontleg_coordinates)
	pyrosim.Send_Cube(name="FrontLeg", pos=frontLeg_coordinates , size=link_size)
	pyrosim.End()

def Generate_Brain():
	pyrosim.Start_NeuralNetwork("brain.nndf")
	pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
	pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
	pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
	pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
	pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
	sensorNeurons = [0,1,2]
	motorNeurons = [3,4]
	for i in sensorNeurons:
		for j in motorNeurons:
			pyrosim.Send_Synapse(sourceNeuronName = i, targetNeuronName = j, weight = np.random.uniform(-1,1))
	pyrosim.End()


Generate_Body()
Generate_Brain()
