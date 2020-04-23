from Position import Position

# Class that defines a collected data sample at a given point in time

class Sample:
    float(time)
    simcarPos = Positon()
    simcarHeading = Position()
    float(simcarFracIndex)
    float(simcarSpeed)
    long(simcarRoadIndex)
    nearPoint = Position()
    farPoint = Position()
    carPoint = Position()
    float(steerAngle)
    float(accelerator)
    float(brake)
    autocarPos = Position()
    autocarHeading = Position()
    float(autocarFracIndex)
    float(autocarSpeed)
    bool(autocarBraking)
    # LocationChunk eyeLocation;
    # LocationChunk handLocation;
    bool(handMoving)
    bool(listening)
    bool(inDriveGoal)
    
    int(event)
    float(lanepos)

    def toString(self):
        return_string = "[" + str(time) + "\t" + str(simcarPos) + "\t" + str(simcarHeading) + "\t" + str(simcarFracIndex) + "\t" + str(simcarSpeed) + "\t" + str(simcarRoadIndex) + "\t" + str(nearPoint) + "\t" + str(farPoint) + "\t" + str(carPoint) + "\t" + str(steerAngle) + "\t" + str(accelerator) + "\t" + str(brake) + "\t" + str(autocarPos) + "\t" + str(autocarHeading) + "\t" + str(autocarFracIndex) + "\t" + str(autocarSpeed) + "]"
        return return_string
    