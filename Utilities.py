import math
import time
import traceback

from random import randrange


class Utilities:
    # From java
    # static DecimalFormat df1 = new DecimalFormat ("#.0")
	# static DecimalFormat df2 = new DecimalFormat ("#.00")
	# static DecimalFormat df3 = new DecimalFormat ("#.000")
	# static DecimalFormat df4 = new DecimalFormat ("#.0000")
	# static DecimalFormat df5 = new DecimalFormat ("#.0000")

    # Need to look into random
    random = random(time.time_ns * 1000)

    def sign(self, x):
        return_x = 1
        if (x >= 0):
            return (return_x)
        else:
            return (return_x * -1)
        
    def sqr(self, x):
        sqaure = x * x
        return (sqaure)

    def rotationAngle(self, hx, hz):
        angle = -180 * (math.atan2(hz, hx)) / math.pi
        return (angle)

    def deg2rad(self, x):
        rad = x * (math.pi / 180.0)
        return (rad)
    def rad2deg(self, x):
        deg = x * (180.0 / math.pi)
        return (deg)

    def mps2mph(self, x):
        mph = x * 2.237
        return (mph)
    def mph2mps(self, x):
        mps = x / 2.237
        return (mps)
    def mph2kph(self, x):
        kph = x * 1.609
        return (kph)
    def kph2mph(self, x):
        mph = x / 1.609
        return (mph)

    def sec2ms(self, x):
        ms = int(round(x * 1000))
        return (ms)
    
    #Need to look into function for randomize, uniqueOutputFile, and setFullScreen
    def randomize(self, s):
		s2 = ""
		while (! s.equals(""))
		    r = int(random.nextInt (s.length()))
			s2 = s2 + s.substring(r, r+1)
			s = s.substring (0,r) + s.substring (r+1,s.length())
		return s2
	
    #Look/Fix up this function
    def uniqueOutputFile(self, str(name)):
        num = 1
        file = os.path.join(parentDir, filename)
        while(file.exists()):
            filename = name + str(num) + ".txt"
            file = open(filename)
            num = num + 1
        
        stream = None
        try:
            stream = PrintStream(FileOutputStream(file))
        except:
            traceback.print_exc()

        return (stream)

    # Find Frame() and GraphicsEnvironment/GraphicsDevice
    def setFullScreen(self, frame = Frame()):
        ge = GraphicsEnvironment(GraphicsEnvironment.getLocalGraphicsEnvironment())
        device = GraphicsDevice(ge.getDefaultScreenDevice())
        device.setFullScreenWindow(frame)
        frame.validate()



