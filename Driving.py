from Coordinate import Coordinate
from Env import Env
from Simcar import Simcar
from Simulation import Simulation

import math
import traceback

# Main Driving task class that sets up the simulation and starts the periodic updates

# Java file says 'class Driving extends actr.task.Task;
class Driving:
    # Need to find out how to declare these variables
    Simulator simulator = None
    JLabel nearLabel, carLabel, keypad    
    simulation = Simulation()

    def __init__(self):
        self.scale = 0.6
        self.steerFactor_dfa = (16 * self.scale)
        self.steerfactor_dna = (4 * self.scale)
        self.steerFactor_na  = (3 * self.scale)
        self.steerFactor_fa  = (0 * self.scale)
        self.accelFactor_thw  = (1 * .40)
        self.accelFactor_dthw = (3 * .40)
        self.steerNaMax = .07
        self.thwFollow = 1.0
        self.thwMax = 4.0

        self.startTime = 0
        self.endTime = 60
        self.accelBrake = 0
        self.speed = 0

        self.minX = 174
        self.maxX = (238+24)
        self.minY = 94
        self.maxY = (262+32)
        self.centerX = (self.minX + self.maxX)/2
        self.centerY = (self.minY + self.maxY)/2

    def Driving(self):
        super()
        nearLabel = JLabel(".")
        carLabel = JLabel("X")
        keypad = JLabel("*")

    def start(self):
        simulation = Simulation(getModel())

        if(getModel().getRealTime()):
            setLayout(BoderLayout())
            if(simulator == None):
                simulator = Simulator()
            add(simulator, BorderLayout.CENTER)
            simulator.useSimulation(simulation)
        else:
			add(nearLabel)
			nearLabel.setSize(20, 20)
			nearLabel.setLocation(250, 250)
			add(carLabel)
			carLabel.setSize(20, 20)
			carLabel.setLocation(250, 250)
			add(keypad)
			keypad.setSize(20, 20)
			keypadX = 250 + int(actr.model.Utilities.angle2pixels (10.0))
			keypad.setLocation(keypadX, 250)

        # Need to look into the "getModel()" function
        getModel().runCommand ("(set-visual-frequency near .1)")
		getModel().runCommand ("(set-visual-frequency car .1)")

		accelBrake = 0
		speed = 0

		getModel().getVision().addVisual ("near", "near", "near", nearLabel.getX(), nearLabel.getY(), 1, 1, 10)
		getModel().getVision().addVisual ("car", "car", "car", carLabel.getX(), carLabel.getY(), 1, 1, 100)
		getModel().getVision().addVisual ("keypad", "keypad", "keypad", keypad.getX(), keypad.getY(), 1, 1)

		addPeriodicUpdate (Env.sampleTime)

    def update(self, float(time)):
        if (time <= endTime):
            simulation.env.time = time - startTime
            simulation.update()
            updateVisuals()
        else:
            getModel().stop()

    def updateVisuals(self):
        env = Env()
        env = simulation.env
        if(env.simcar.nearPoint != None):
            cn = Coordinate()
            cn = env.world2image(env.simcar.nearPoint)
            cc = Coordinate()
            cc = env.world2image(env.simcar.carPoint)
            # cc = env.world2image(env.simcar.farPoint)

            if (cn == None or cc == None):
                env.done = True
            else:
                nearLabel.setLocation(cn.x, cn.y)
                carLabel.setLocation(cc.x, cc.y)
				getModel().getVision().moveVisual ("near", cn.x, cn.y)
				getModel().getVision().moveVisual ("car", cc.x, cc.y)
                # getModel().getVision().moveVisual ("near", cn.x+5, cn.y+10)
                # getModel().getVision().moveVisual ("car", cc.x+5, cc.y+10)
				speed = env.simcar.speed       

    def minSigned(self, x, y):
        return_min = min(x,y)
        return_max = max(x,y)
        if(x >= 0):
            return float(return_min)
        else:
            return float(return_max)

    def doSteer(self, na, dna, dfa, dt):
        simcar = Simcar()
        simcar = simulation.env.simcar
        if(simcar.speed >= 10.0):
            dsteer = float((dna * steerFactor_dna) + (dfa * steerFactor_dfa) + (minSigned (na, steerNaMax) * steerFactor_na * dt))
            dsteer *= simulation.driver.steeringFactor
			simcar.steerAngle += dsteer
        else:
            simcar.steerAngle = 0
        
    def doAccelerate(self, fthw, dthw, dt):
        simcar = Simcar()
        simcar = simulation.env.simcar
        if(simcar.speed >= 10.0):
            dacc = float((dthw * accelFactor_dthw) + (dt * (fthw - thwFollow) * accelFactor_thw)
            accelBrake += dacc
			accelBrake = minSigned(accelBrake, 1.0))
        else:
            accelBrake = 0.65 * (simulation.env.time / 3.0)
            accelBrake = minSigned(accelBrake, 0.65)

        if(accelBrake >= 0):
            simcar.accelerator = accelBrake
        else:
            simcar.accelerator = 0

        if(accelBrake < 0):
            simcar.brake = -1 * accelBrake
        else:
            simcar.brake = 0

    def isCarStable(self, na, nva, fva):
        f = 2.5
        return (math.abs(na) < .025*f) and (math.abs(nva) < .0125*f) and (math.abs(fva) < .0125*f)

    def image2angle(self, x, d):
        env = Env()
        env = simulation.env
        px = env.simcar.p.x + (env.simcar.h.x * d)
        pz = env.simcar.p.z + (env.simcar.h.z * d)
        im = Coordinate()
        im = env.world2image(Position(px, pz))
        try:
            return math.atan2(0.5*(x-im.x), 450)
        except:
            return 0
        
    # Compare next three functions to java
    # Look at Iterator<String> it    
    def eval(self, it):
        it.next()
        cmd = it.next()
        if(cmd.equals ("do-steer")):
            na = Double.valueOf(it.next())
            dna = Double.valueOf(it.next())
            dfa = Double.valueOf(it.next())
            dt = Double.valueOf(it.next())
            doSteer(na, dna, dfa, dt)
        elif(cmd.equals("do-accelerate")):
            fthw = Double.valueOf(it.next())
            dthw = Double.valueOf(it.next())
            dt - Double.valueOf(it.next())
            doAccelerate(fthw, dthw, dt)

    def evalCondition(self, it):
        it.next()
        cmd = it.next()
        if(cmd.equals("is-car-stable") or cmd.equals("is-car-not-stable")):
            na = Double.valueOf(it.next())
            nva = Double.valueOf(it.next())
            fva = Double.valueOf(it.next())
            b = isCarStable(na, nva, fva)
            if(cmd.equals("is-car-stable") == True):
                return b
            else:
                return (not b)
        
    def bind(self, it):
        try:
            it.next()
            cmd = it.next()
            if(cmd.equals("image->angle")):
                x = Double.valueOf(it.next())
                d = Double.valueOf(it.next())
                return image2angle(x,d)
            elif(cmd.equals("mp-time")):
                return simulation.env.time
            elif(cmd.equal("get-thw")):
                fd = Double.valueOf(it.next())
                v = Double.valueOf(it.next())
                if(v==0):
                    thw = 4.0
                else:
                    thw = fd/v
            elif(cmd.equal("get-velocity")):
                return speed
            else:
                return 0
        except:
            traceback.print_exc()
            sys.exit()
            return 0

    def numberOfSimulations(self):
        return 1

    def analyze(self, tasks, output):
        return None

     
