from ntpath import join
from turtle import position
import matplotlib.pyplot as plt
import numpy as np
import glob
import re

# Get Sensor
sensorData = glob.glob("data/*_sensor.npy")
linkSensor = {}
for data in sensorData:
    pattern = "data(.*?)\_sensor.npy"
    linkName = re.search(pattern, data).group(1)[1:]
    linkSensor[linkName] = np.load(data)
# Get Commands
motorData = glob.glob("data/*_commands.npy")
jointCommands = {}
for data in motorData:
    pattern = "data(.*?)\_commands.npy"
    jointName = re.search(pattern, data).group(1)[1:]
    jointCommands[jointName] = np.load(data)

fig = plt.figure(1)
for jointName, data in jointCommands.items():
    plt.plot(data, label = jointName)
plt.xlabel("Steps")
plt.ylabel("Value in Radians")
plt.title("Motor Commands")
plt.legend(loc = "upper right")
plt.show()

fig = plt.figure(2)
for linkName, data in linkSensor.items():
    plt.plot(data, label = linkName)
plt.xlabel("Steps")
plt.ylabel("Value in Radians")
plt.title("Link Sensor")
plt.legend(loc = "upper right")
plt.show()