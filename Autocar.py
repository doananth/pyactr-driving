from Vehicle import Vehicle
import math

# An automated car that drives itself down the road

class Autocar:
    def __init__(self):
        self.braking = False
        self.lastBrakeTime = None
        self.brakeSpacing = 4   # time between braking events
        self.nextBreakTime = 999999  # static value

    def Autocar(self):
        super ()
        Vehicle.speed = 0

    # Need to look into the "Env env" file to incorporate it 
    def update(self, env):
        if (env.scenario.leadCarBrakes):
            if((not self.braking) and (self.lastBrakeTime + self.brakeSpacing <= env.time)):
                self.braking = True
                self.lastBrakeTime = env.time
            if((self.braking) and (self.lastBrakeTime + 2.0 <= env.time)):
                self.braking = False

        if((env.scenario.simCarConstantSpeed) or (env.simcar.speed < 10.0)):
            self.speed = env.simcar.speed
            Vehicle.fracIndex = env.simcar.fractIndex + 20.0
        else:
            if(env.scenario.leadCarConstantSpeed):
                # Need to look into the function that convers mph to mps & "Env" variable
                fullspeed = Utilities.mph2mps(Env.scenario.leadCarMPH)
            else: 
                # From CSR 2002
                self.speed = 20 + 5 * math.sin(Vehicle.fracIndex/100.0) + 5 * math.sin(13.0 + Vehicle.fracIndex/53.0) + 5 * math.sin(37.0 + Vehicle.fracIndex/141.0)
            
            Vehicle.fracIndex = Vehicle.fracIndex + (speed * Env.sampleTime)
        
            if(Vehicle.fracIndex < env.simcar.fracIndex + 11.0):
                Vehicle.fracIndex = env.simcar.fracIndex + 11.0
        
        # Need to look into the env.road.middle() function
        Vehicle.position_p = env.road.middle(Vehicle.fracIndex)
        Vehicle.position_p.y = 0.65

        # Need to look into the env.road.heading() function
        Vehicle.position_h = env.road.heading(Vehicle.fracIndex)
        
    # Need to find the Graphics g and Env env Classes
    def draw(self, g, env):
        # Declared as Position pos1
        # Need to find the env.road.location function
        pos1 = env.road.location(Vehicle.fracIndex, 2.2)
        pos1.y = 0.0
        # Declared as Coordinate im1
        # Need to find world2image function 
        im1 = env.world2image(pos1)

        # Declared as Position pos2
        pos2 = env.road.location(Vehicle.fracIndex, 2.8)
        pos2.y = 1.0
        # Declared as Coordinate im2
        im2 = env.world2image(pos2)

        # Need to find way to import a color module to set color to blue
        g.setColor(Color.blue)
        g.fillRect (im1.x, im2.y, im2.x-im1.x, im1.y-im2.y)



        

