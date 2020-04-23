# Class that defines the particular scenario represented by the driving environment

class Scenario:
    def __init__(self):
       #super().__init__()
       self.curvedRoad = False
       self.simCarConstantSpeed = True
       self.simCarMPH = 55
       self.leadCarConstantSpeed = True
       self.leadCarMPH = 55
       self.leadCarBrakes = True
       self.drivingMinutes = 15
       self.timeBetweenTrials = 240
       self.baselineOnly = False

    def writeString(self):
        s = (self.curvedRoad if self.curvedRoadTrue else False) + "\t"
        s = s + (self.simCarConstantSpeed if self.simCarConstantSpeed else False) + "\t"
        s = s + str(self.simCarMPH) + "\t"
        s = s + (self.leadCarConstantSpeed if self.leadCarConstantSpeed else False) + "\t"
        s = s + str(self.leadCarMPH) + "\t"
        s = s + (self.leadCarBrakes if self.leadCarBrakes else False) + "\t"
        s = s + self.drivingMinutes + "\t"
        s = s + self.timeBetweenTrials
        return s

        

