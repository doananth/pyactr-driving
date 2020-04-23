from Driver import Driver

# Class that defines useful measures for data collection

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
        return_string = "(" + str(self.taskTime) + ", " + str(self.taskLatDev) + ", " + str(self.taskLatVel) + ", " + str(self.brakeRT) + ", " + str(self.headingError) + ", " + str(self.taskSpeedDev) + ")"
		return return_string