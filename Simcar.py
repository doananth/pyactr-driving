from Driver import Driver
from Env import Env
from Road import Road
from Utilities import Utilities
from Vehicle import Vehicle

import math

# Class for the driver's own vehicle and its controls

class Simcar:
    driver = Driver()

    __init__(self, driver, env = Env()):
        super()
        self.driver = driver

        steerAngle = 0
        accelerator = 0
        brake = 0
        speed = 0

    order = 6
    max_order = 10
    gravity = 9.8
    air_drag_coeff = 0.25
    engine_max_watts = 106000
    brake_max_force = 8000
    f_surface_friction = 0.2
    lzz = 2618
    ms = 1175
    a = 0.946
    b = 1.719
    caf = 48000
    car = 42000
    y = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0]
    dydx = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0]
    yout = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0]
    heading = -999
    heading1 = -999
    heading2 = -999
    float(car_heading)
    float(car_accel_pedal)
    float(car_brake_pedal)
	float(car_deltaf)
	float(car_steer)
	float(car_speed)
	float(car_ke)

    def derivs(self, y, dydx):
        phi = y[1]
        r = y[2]
        beta = y[3]
        ke = y[4]
        u = 0
        if(ke > 0):
            u = math.sqrt(ke*2/ms)
        else: 
            u = 0
        dydx[1] = r
        if(u > 5):
            dydx[2] = (2.0 * a * caf * deltaf - 2.0 * b * car * deltar - 2.0 * (a * caf - b * car) * beta - (2.0 * (a*a * caf + b*b * car) * r / u)) / lzz
            dydx[3] = (2.0 * caf * deltaf + 2.0 * car * deltar - 2.0 * (caf + car) * beta - (ms * u + (2.0 * (a * caf - b * car) / u)) * r) / (ms * u)
        else:
            dydx[1] = 0.0
            dydx[2] = 0.0
            dydx[3] = 0.0

        pengine = car_accel_pedal * engine_max_watts 
        fbrake = car_brake_pedal * brake_max_force
        fdrag = (f_surface_friction * ms * gravity) + (air_drag_coeff * u)
        dydx[4] = pengine - fdrag * u - fbrake * u
        dydx[5] = u * math.cos(phi)
        dydx[6] = u * math.sin(phi)

    def rk4(self, n, x, h):
        dym = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0]
        dyt = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0]
        yt = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0]
        hh = h * 5
        h6 = h/6
        int(i)

        for(i in range (0, n)):
            yt[i] = y[i] + hh*dydx[i]
            i += 1
        derivs(yt, dyt)
        for(i in range (0,n)):
            yt[i] = y[i] + hh*dyt[i]
            i += 1
        derivs(yt, dym)
        for(i in range (0,n)):
            yt[i] = y[i] + h*dym[i]
            dym[i] = dym[i] + dyt[i]
            i += 1
        derivs(yt, dyt)
        for(i in range (0,n)):
            yout[i] = y[i] + h6*(dydx[i] + dyt[i] + 2.0*dy,[i])

    def updateDynamics(self, env = Env()):
        road = Road()
        road = env.road
        time = env.time
        sampleTime = Env.CONST_sampleTime

        if(heading2 == -999.0):
            heading = heading1 = heading2 = math.atan2(h.z, h.x)
            yout[1] = y[1] = car_heading = heading
            yout[2] = y[2] = 0.0
            yout[3] = y[3] = 0.0
            yout[4] = y[4] = car_ke = 50000 # 0.0; # kinetic energy > 0, otherwise unstable at start
            yout[5] = y[5] = p.x
            yout[6] = y[6] = p.z
            if(car_ke > 0.0):
                car_speed = car.sqrt(2.0 * car_ke/ms)
            else:
                car_speed = 0.0
        
        car_steer = steerAngle
		car_accel_pedal = accelerator
		car_brake_pedal = brake

        # original had lines below; changing to linear steering function
		# if (car_steer < 0.0): car_deltaf = -0.0423 * math.pow(-1.0*car_steer, 1.3)
		# else: car_deltaf =  0.0423 * math.pow(car_steer,1.3)
        car_deltaf = 0.0423 * car_steer

        forcing = 0.125 * (0.01 * math.sin(2.0 * 3.14 * 0.13 * time + 1.137) + 0.005 * math.sin(2.0 * 3.14 * 0.47 * time + 0.875))   
        car_deltaf += forcing

        derivs(y, dydx)
        rk4(order, time, sampleTime)

        y[1] = car_heading = yout[1]
		y[2] = yout[2]
		y[3] = yout[3]
		y[4] = car_ke = yout[4]
		y[5] = p.x = yout[5]
		y[6] = p.z = yout[6]

        if (car_ke > 0.0):
            car_speed = math.sqrt(2.0 * car_ke / ms)
        else:
            car_speed = 0.0
        
        h.x = math.cos(car_heading)
        h.z = math.sin(car_heading)

        heading2 = heading1
        heading1 = heading1
        heading = car_heading

        speed = car_speed

        if (Env.scenario.simCarConstantSpeed):
            fullspeed = Utilities.mph2mps(Env.scenario.simCarMPH)
            if (speed < fullspeed):
                speed += 0.1
            else:
                speed = fullspeed
        else:
            speed = car_speed

        i = max(1, roadIndex)
        newi = i
        # Check out .subtract(p)
        nearloc = Position(road.middle (i)).subtract(p)
        norm = (nearloc.x * nearloc.z) + (nearloc.z * nearloc.z) # error in lisp here
        mindist = norm
        done = False

        while(not done):
            i += 1
            nearloc = (road.middle (i)).subtract(p)
            norm = (nearloc.x * nearloc.x) + (nearloc.z * nearloc.z) # error in lisp here
            if (norm < mindist):
                mindist = norm
                newi = i
            else:
                done = True
        
        vec1 = Position(road.middle (newi)).subtract (p)
        vec2 = Position(road.middle (newi)).subtract (road.middle (newi-1))
        dotprod = - ((vec1.x * vec2.x) + (vec1.z * vec2.z))
        float(fracdelta)
        if (dotprod < 0):
            newi -= 1
            fracdelta = 1.0 + dotprod
        else:
            fracdelta = dotprod
        
        fracIndex = newi + fracdelta
        roadIndex = newi

        def update(self, env = Env()):
            updateDynamics(env)

            nearPoint = env.road.nearPoint(self, 2)
            farPOint = env.road.farPoint(self, None, 2)
            carPoint = env.autocar.p

        def draw(self, g = Graphics(), env = Env()):
            dashHeight = 80
            # Look into setting colors and fillrect
            g.setColor(color.black)
            g.fillRect (0, Env.envHeight - dashHeight, Env.envWidth, dashHeight)

            steerX = 160
            steerY = Env.CONST_envHeight - 20
            steerR = 50
            # Look into setting color
            g.setColor(color.darkGray)
            # Look into the two lines below
 		    # Graphics2D g2d = (Graphics2D) g
		    # AffineTransform saved = g2d.getTransform()
            g2d.translate (steerX, steerY)
		    g2d.rotate (steerAngle)
		    g2d.setStroke (new BasicStroke (10))
		    g2d.drawOval (-steerR, -steerR, 2*steerR, 2*steerR)
		    g2d.fillOval (-steerR/4, -steerR/4, steerR/2, steerR/2)
		    g2d.drawLine (-steerR, 0, +steerR, 0)
		    g2d.setTransform (saved)

        devscale = 0.0015
        devx = -0.7
        devy = 0.5
        def ifc2gl_x(self, float(x)):
            return devx + (devscale * -1*(x - Driving.centerX))
        def ifc2gl_y(self, float(y)):
            return devy + (devscale * -1*(y - Driving.centerY))
        def gl2ifc_x(self, float(x)):
            return Driving.centerX - ((x - devx) / devscale)
        def gl2ifc_y(self, float(y)):
            return Driving.centerY - ((y - devy) / devscale)          


