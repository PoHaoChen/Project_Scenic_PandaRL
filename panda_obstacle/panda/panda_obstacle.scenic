model scenic.simulators.webots.model
from numpy import random

room_region = RectangularRegion(0 @ 0, 0, 2, 2)
workspace = Workspace(room_region)

class Floor(Object):
    width: 2
    length: 2
    height: 0.01
    position: (0,0,0.64495)
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

floor = new Floor
c1 = new Object at (0.45, 0, 0.7), with allowCollisions True
c2 = new TARGET on floor
require distance from c1 to c2 <= 0.5

terminate after 15*300 steps # 15*STEPS