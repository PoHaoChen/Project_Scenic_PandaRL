model scenic.simulators.webots.model
from numpy import random

room_region = BoxRegion(dimensions=(1,1,1), position=(0,0,0.68005))
workspace = Workspace(room_region)

class Floor(Object):
    width: 2
    length: 2
    height: 0.01
    position: (0,0,0.58005)
    color: [0.785, 0.785, 0.785]

class centerObj(WebotsObject):
    webotsName: "CENTER"
    width: 0.000001
    length: 0.000001
    height: 0.000003
    position: (0,0,0.5)
    shape: CylinderShape()

class OBSTACLE(WebotsObject):
    webotsName: "OBSTACLE"
    width: 0.02
    length: 0.02
    height: 0.1
    shape: CylinderShape()

class TARGET(WebotsObject):
    webotsName: "TARGET"
    width: 0.02
    length: 0.02
    height: 0.1
    shape: CylinderShape()

target = new TARGET in workspace

terminate after 15*300 steps # 15*STEPS