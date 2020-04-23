from Driver import Driver
from Env import Env
from Model import Model
from Position import Position
from Results import Results
from Road import Road
from Sample import Sample
from Scenario import Scenario

# Need to import Graphics()
# Find way to do vector<samples> for line 19
import numpy as np
import math

# Class that defines the entire simulation including the driver, scenario, and samples

class Simulation:
    model = Model()
    driver = Driver()
    scanario = Scenario()
    env = Env()
    env = None
    # Find way to do vector<samples> for line below with correct import
    samples = np.array()
    results = Results()
    results = None

    def Simulation(self, model):
        self.model = model
        driver = Driver(model, "Driver", 25, float(1.0), float(1.0))
        scenario = Scenario()
        env = Env(driver, scenario)
        # samples.add(recordSample(env))

    # Find way for syncrhonized to work
    def	synchronized_update(self):
		self.env.update()
		# samples.add (recordSample (env))

    # analyze() defined below
    def getResults(self):
        self.results = analyze()
        return self.results

    def numSamples(self):
        return self.samples.size()

    def recordSample(self, env):
        s = Sample()
        s.time = env.time
        s.simcarPos = env.simcar.p.myclone()
		s.simcarHeading = env.simcar.h.myclone()
		s.simcarFracIndex = env.simcar.fracIndex
		s.simcarSpeed = env.simcar.speed
		s.simcarRoadIndex = env.simcar.roadIndex
        if(env.simcar.nearPoint == None):
			s.nearPoint = env.simcar.nearPoint.myclone()
			s.farPoint = env.simcar.farPoint.myclone()
			s.carPoint = env.simcar.carPoint.myclone()
 		s.steerAngle = env.simcar.steerAngle
		s.accelerator = env.simcar.accelerator
		s.brake = env.simcar.brake
		s.autocarPos = env.autocar.p.myclone()
		s.autocarHeading = env.autocar.h.myclone()
		s.autocarFracIndex = env.autocar.fracIndex
		s.autocarSpeed = env.autocar.speed
		s.autocarBraking = env.autocar.braking
        s.lanepos = env.road.vehicleLanePosition(env.simcar)

        return s

    # Find way for syncrhonized to work
    def synchronized_draw(self, g = Graphics()):
        if(self.env != None):
            env.draw(g)
    
    def rotAngle(self, hx, hz):
        return (-180 * (math.atan2(hz,hx))/math.pi)

    def headingError(self, s = Sample()):
        s2 = Road.Segment()
        s2 = env.road.getSegment(s.simcarRoadIndex)
        s1 = Road.Segment()
        s1 = self.env.road.getSegment(s.simcarRoadIndex - 1)
        rh = Position()
        rh = rh.normalize()

        return (abs(rotAngle(rh.x, rh.z) - rotAngle(s.simcarHeading.x, s.simcarHeading.z)))
        
    def lookingAhead(self, s):
        return True
    
    def analyze(self):
        startTime = float(0)
		stopTime = float(-1000)

		numTasks = 0
		numTaskSamples = 0
		sumTime = float(0)
		sumLatDev = float(0)
		sumLatVel = float(0)
		sumSpeedDev = float(0)
		numTaskDetects = float(0)
        numTaskDetectsCount = float(0)
		sumBrakeRTs = float(0)
        numBrakeRTs = float(0)
        lastBrakeTime = float(0)
		brakeEvent = False
		headingErrors = float([len(samples)])
	    laneViolations = 0
		lvDetected = False

        for (i in range (1, len(self.samples))):
            s = Sample()
            s = samples.elementAt(i)
            sprev = Sample()
            sprev = samples.elementAt(i - 1)

            if((s.event > 0) or (s.time < stopTime + 5)):
                numTaskSamples += 1
                latdev = 3.66 * (s.lanepos - 2.5)
                sumLatDev += (latdev * latdev)
				sumLatVel += abs((3.66 * (s.lanepos - sprev.lanepos)) / Env.sampleTime)
				sumSpeedDev += (s.simcarSpeed - s.autocarSpeed) * (s.simcarSpeed - s.autocarSpeed)

                if((s.event > 0) or (s.time < stopTime)):
                    numTaskDetectsCount += 1
                    if(lookingAhead(s)):
                        numTaskDetects += 1

                if (((s.events > 0) or (s.time < stopTime)) and (not brakeEvent) and (s.autocarBraking and not sprev.autocarBraking)):
                    brakeEvent = True
                    lastBrakeTime = s.time
                if (brakeEvent and not s.autocarBraking):
                    brakeEvent = False
                if (brakeEvent and (s.brake > 0)):
                    sumBrakeRTs += (s.time - lastBrakeTime)
                    numBrakeRTs += 1
                    brakeEvent = False
                
                headingErrors[numTaskSamples - 1] = headingError(s)
                if (not lvDetected and (abs(latdev) > (1.83 - 1.0))):
                    laneViolations += 1
                    lvDetected = True

                if((s.event == 1) and (sprev.event == 0)):
                    startTime = s.time
                    lvDetected = False
                    brakeEvent = False
                elif((s.event == 0) and (sprev.event == 1)):
                    numTasks += 1
                    stopTime = s.time
                    sumTime += (stopTime - startTime)

            r = Results()
            r.driver = self.driver
            r.taskLatDev = math.sqrt(sumLatDev / numTaskSamples)
		    r.taskLatVel  = sumLatVel / numTaskSamples
		    r.taskSpeedDev = math.sqrt(sumSpeedDev / numTaskSamples)
            
            if(numTasks == 0):
                r.detectionError = 0
            else:
                r.detectionError = (1.0 - (1.0 * numTaskDetects / numTaskDetectsCount))
            
            if(numBrakeRTs == 0):
                r.brakeRT = 0
            else:
                r.brakeRT = (sumBrakeRTs / numBrakeRTs)

		    Arrays.sort(headingErrors, 0, numTaskSamples-1)
		    heIndex = int(0.9 * numTaskSamples)
		    r.headingError = headingErrors[heIndex]

		    r.laneViolations = laneViolations

            return r
            




	
