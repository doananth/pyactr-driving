from Driver import Driver
class Results:

    driver = Driver()

    def __init__(self):
	    self.taskTime = None
	    self.taskLatDev = None
	    self.taskLatVel = None
	    self.headingError = None
	    self.laneViolations = None
	    self.taskSpeedDev = None
	    self.detectionError = None
	    self.brakeRT = None
    
    def toString(self):
        return_string = ("(" + self.taskTime + ", " + self.taskLatDev + ", " + self.taskLatVel + ", " + self.brakeRT + ", " + self.headingError + ", " + self.taskSpeedDev + ")")