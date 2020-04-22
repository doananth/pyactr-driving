from Scenario import Scenario
from Simcar import Simcar
from Road import Road
from Autocar import Autocar
from Driver import Driver
from Road import Road
from Coordinate import Coordinate
from Position import Position

# Need to import 'Graphics' file

class Env:
    scenario = Scenario() 
    scenario = None
    road = Road()
    autocar = Autocar()
    
    time = 0
    CONST_sampleTime = 0.050

    CONST_envWidth = 640
    CONST_envHeight = 360 # 444 # 360
    CONST_heightAdjust = 50

    CONST_simWidth = 640 # 1440 # 640
    CONST_simHeight = 360 # 1000 # 360

    def __init__(self, driver = Driver(), s = Scenario()):
        scenario = s 
        road = Road()
        road.startup()

        simcar = Simcar(driver, self)
        road.vehicleReset(simcar, 2, 100)

        autocar = Autocar()
        road.vehicleReset(autocar, 2, 120)

        done = False
    
    def update(self):
        self.simcar.update(self)
        self.autocar.update(self)

    def draw(self, g = Graphics()):
        g.clipRect(0, 0, CONST_envWidth, CONST_envHeight)

        # Need to find out where to set graphics color
        g.setColor(Color(146, 220, 255)))
        g.fillRect(0, 0, CONST_envWidth, CONST_envHeight)

        # Need to look into world2image
        # Coordinate vp = world2image (road.location (simcar.fracIndex + 1000, 2.5))
        g.setColor(Color(0, 125, 15))
        g.fillRect(0, vp.y, CONST_envWidth, CONST_envHeight)

        self.road.draw(g, self)
        self.autocar.draw(g, self)
        self.simcar.draw(g, self)

    simViewAH = 0.13
	simViewSD = -.37
	simViewHT = 1.15
	simFocalS = 450
	simOXR = 1.537 / (1.537 + 2.667) # (1.2 + simViewSD) / (1.2 + 1.2)
	simOYR = (2.57 - simViewHT) / 2.57 # (1.67 + .2 - simViewHT) / 1.67
	simNear = 1.5 # 1.5 # 2.95
    simFar = 1800.00
    
    def world2image(self, world = Position()):
        hx = self.simcar.hx
		hz = self.simcar.hz
		px = self.simcar.px + ((hx * simViewAH) - (hz * simViewSD))
		py = simViewHT
		pz = self.simcar.pz + ((hz * simViewAH) + (hx * simViewSD))
		wx1 = world.x - px
		wy1 = world.y
		wz1 = world.z - pz
		wx = (hx * wz1) - (hz * wx1)
		wy = py - wy1
		wz = (hz * wz1) + (hx * wx1)
		ox = simOXR * CONST_envWidth
		oy = simOYR * CONST_envHeight

        if (wz > 0):
            imx = round(ox + ((simFocalS * wx) / wz))
            imy = round(oy + ((simFocalS * wy) / wz))
            imd = wz
            imy = imy - CONST_heightAdjust
            return Coordinate(imx, imy, imd)
        else:
            return None
            
    


        
