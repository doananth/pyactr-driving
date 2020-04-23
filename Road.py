from Coordinate import Coordinate
from Env import Env
from Position import Position
from Vehicle import Vehicle
from Simcar import Simcar

import math

# Primary class that defines a road

class Road:
    segments = segments.zeros()
    lanes = 3
    def __init__(self):

    class Segment:
        left, middle, right = Position()
        h = Position()
        l_left, l_right = Position()
        ll_left, rr_right = Position()
        lll_left, rrr_right = Position()
        ll_mid, lr_mid, rl_mid, rr_mid = Position()
        l_lmid, r_lmid, l_rmid, r_rmid = Position()

        def Segment(self, a1, a2, a3, a4, a5, a6):
            left = Position(a1, a2)
            middle = Position(a3, a4)
            right = Position(a5, a6)

            h = Position(right.x - left.x, right.z - left.z)
            h = h.normalize()

            HALF_STRIPW = 0.08
            STRIPW = (2 * HALF_STRIPW)
            SHOULDER = 1.5
            WALL = 40

            dx = 0.05 * h.x
            dz = 0.05 * h.z

			l_left = Position(left.x - (2 * STRIPW * h.x) - dx, left.z  - (2 * STRIPW * h.z) - dz)
			r_right = Position(right.x + (2 * STRIPW * h.x) + dx, right.z + (2 * STRIPW * h.z) + dz)

			ll_left = Position(left.x - (SHOULDER * h.x) - dx, left.z - (SHOULDER * h.z) - dz)
			rr_right = Position(right.x + (SHOULDER * h.x) + dx, right.z + (SHOULDER * h.z) + dz)

			lll_left = Position(left.x - (WALL * h.x), left.z - (WALL * h.z))
			rrr_right = Position(right.x + (WALL * h.x), right.z + (WALL * h.z))

			ll_mid = Position(middle.x - (3 * HALF_STRIPW * h.x), middle.z - (3 * HALF_STRIPW * h.z))
			lr_mid = Position(middle.x - (HALF_STRIPW * h.x), middle.z - (HALF_STRIPW * h.z))
			rl_mid = Position (middle.x + (HALF_STRIPW * h.x), middle.z + (HALF_STRIPW * h.z))
			rr_mid = Position(middle.x + (3 * HALF_STRIPW * h.x), middle.z + (3 * HALF_STRIPW * h.z))

            if(lanes == 4):
                l_lmid = Position((0.5 * ll_mid.x + 0.5 * left.x) - HALF_STRIPW * h.x, (0.5 * ll_mid.z + 0.5 * left.z) - HALF_STRIPW * h.z)
				r_lmid = Position((0.5 * ll_mid.x + 0.5 * left.x) + HALF_STRIPW * h.x, (0.5 * ll_mid.z + 0.5 * left.z) + HALF_STRIPW * h.z)

				l_rmid = Position((0.5 * rr_mid.x + 0.5 * right.x) - HALF_STRIPW * h.x, (0.5 * rr_mid.z + 0.5 * right.z) - HALF_STRIPW * h.z)
				r_rmid = Position((0.5 * rr_mid.x + 0.5 * right.x) + HALF_STRIPW * h.x, (0.5 * rr_mid.z + 0.5 * right.z) + HALF_STRIPW * h.z)
            elif(lanes == 3):
            	l_lmid = Position((0.666 * middle.x + 0.334 * left.x) - HALF_STRIPW * h.x, (0.666 * middle.z + 0.334 * left.z) - HALF_STRIPW * h.z)
				r_lmid = Position((0.666 * middle.x + 0.334 * left.x) + HALF_STRIPW * h.x, (0.666 * middle.z + 0.334 * left.z) + HALF_STRIPW * h.z)

				l_rmid = Position((0.666 * middle.x + 0.334 * right.x) - HALF_STRIPW * h.x, (0.666 * middle.z + 0.334 * right.z) - HALF_STRIPW * h.z)
				r_rmid = Position((0.666 * middle.x + 0.334 * right.x) + HALF_STRIPW * h.x, (0.666 * middle.z + 0.334 * right.z) + HALF_STRIPW * h.z)
    

    def startup(self):
        curved = Env.scenario.curvedRoad
        p = Position(0.0, 0.0, 0.0)
        h = Position(1.0, 0.0, 0.0)
        h = h.normalize()

        seglen = 200
        segcount = 0
        curving = False
        da = 0
        dascale = 0.02
        d = lanes * 3.66/2.0

        for i in range(0, 40000):
            if (segcount >= seglen):
                segcount = 0
                seglen = 100
                if(curved):
                    curving = not curving
                    if (curving):
                        if (da > 0):
                            da = -1 * dascale * 17
                        else:
                            da = 1 * dascale * 17
            
            if (curving):
                h = h.rotate(da)

            p = p.add(h)
            s = Segment(p.x + d * h.z, p.z - d * h.x, p.x, p.z, p.x - d * h.z, p.z + d * h.x)
            segments.addElement(s)
            segcount = segcount + 1
            i = i + 1

    def getSetment(self, i):
        return(From(segments).elementAt(i))

    def location(self = Position(), fracIndex, lanePos):
        i = (math.floor(fracIndex))
        r = fracIndex - i
        laner = (lanePos - 1) / 3

        #Look into getSetment.left/right for the if/else statement
        if(i == fracIndex):
            locL = Position(getSegment(i).left)
            locR = Position(getSegment(i).right)
            return (locL.average(locR, laner))
        else:
            loc1L = Position(getSegment(i).left)
            loc1R = Position(getSegment(i).right)
            loc1 = loc1L.average(loc1R, laner)
            loc2L = Position(getSegment(i + 1).left)
            loc2R = Position(getSegment(i + 1).right)
            loc2 = loc2L.average(loc2R, laner)    
            return (loc1.average(loc2, r))

    def left(self, fracIndex):
         return (location(fracIndex, 4))        

    def left(self, fracIndex, lane):
         return (location(fracIndex, lane + 1))
    
    def middle(self, fracIndex):
         return (location(fracIndex, 2.5))        

    def middle(self, fracIndex, lane):
         return (location(fracIndex, lane + 0.5))
               
    def right(self, fracIndex):
         return (location(fracIndex, 1))        

    def right(self, fracIndex, lane):
         return (location(fracIndex, lane))
        
    def heading(self, fracIndex):
        locdiff = Position(middle (fracIndex + 1)).math.subtract(middle(fracIndex - 1))
        return (normalize(locdiff))

    def vehicleReset(self, v = Vehicle(), lane, fracIndex):
        p = Position(middle(fracIndex, lane))
        h = Position(heading(fracIndex))
        v.position_p.x = p.x
        v.position_p.z = p.z
        v.position_h.x = h.x
        v.position_h.x = h.x
        v.fracIndex = fracIndex

    # Boolean 
    def sign(self, x):
        return (x >= 0)

    def sqr(self, x):
        result = x * x
        return (result)

    def vehicleLanePosition(self, v = Vehicle()):
        i = v.fracIndex
        lloc = Position(left(i))
        rloc = Position(right(i))
        head = Position(head(i))
        ldx = head.x * (v.position_p.z - rloc.z)
        ldx = head.z * (v.position_p.x - rloc.x)
        wx = head.x * (lloc.z - rloc.z)
        wz = head.z * (lloc.x - rloc.x)
        ldist = abs(ldx) - abs(ldz)
        width = abs(wx) - abs(wz)
        lanepos = (ldist / width) * 3

        if(abs(wx) > abs(wz) and (sign(ldx) != sign(wx)) or (abs(wz) > abs(wx) and (sign(ldz) != sign(wz)):
            lanepos = lanepos - 1

        lanepos = lanepos + 1

        return (lanepos)
    
    def vehicleLane (self, v = Vehicle()):
        return (int(math.floor(vehicleLanePosition(v))))

    nearDistance = 10.0
    farDistance = 100.0
    nearTime = 0.5
    farTime = 4.0

    def nearPoint(self, simcar = Simcar()):
        return (Position(middle(simcar.fracIndex + nearDistance)))
    
    def nearPoint(self, simcar = Simcar(), lane):
        return (Position(middle(simcar.fracIndex + nearDistance, lane)))

    fpText = ""
    fpTPfracIndex = 0

    def farPoint(self, simcar = Simcar(), autocars, lane):
        fracNearestRP = simcar.fracIndex
        nearestRP = int(math.floor(fracNearestRP))
        j = nearestRP + 1
        simcarLoc = Position(simcar.position_p.x, simcar.position_p.z)
        turn = 0 #left = 1, right = 2
        aheadMin = nearDistance + 10
        aheadMax = max(aheadMin, simcar.speed * farTime)

        if(lane != 0):
            rln = lane
            lln = lane
        else:
            rln = 1
            lln = 2
        
        # Need to look into left/right().subtract)
        h_l = Position(left(j, lln).subtract(simcarLoc))
		hrd_l = Position(left (j, lln)).subtract (left (j - 1, lln))
		h_r = Position(right (j, rln)).subtract (simcarLoc)
		hrd_r = Position(right (j, rln)).subtract (right (j - 1, rln))

        lxprod1 = (h_l.x *hrd_l.z) - (h_l.z * hrd_l.x)
        norm_lxp1 = abs(lxprod1 / (math.sqrt(sqr(h_l.x) + sqr(h_l.z)) + math.sqrt(sqr(hrd_l.x) + sqr(hrd_l.z))))
        rxprod1 = (h_r.x *hrd_r.z) - (h_r.z * hrd_r.x)
        # Note:  Lisp code below has lxprod1 instead of rxprod1
        norm_rxp1 = abs(rxprod1 / (math.sqrt(sqr(h_r.x) + sqr(h_r.z)) + math.sqrt(sqr(hrd_r.x) + sqr(hrd_r.z))))
        
        go_on = True

        while(go_on):
            j = j + 1

            # left/right().subtract check
			h_l = (left (j, lln)).subtract (simcarLoc)
			hrd_l = (left (j, lln)).subtract (left (j-1, lln))
			h_r = (right (j, rln)).subtract (simcarLoc)
			hrd_r = (right (j, rln)).subtract (right (j-1, rln))

            lxprod2 = (h_l.x * hrd_l.z) - (h_l.z * hrd_l.x)
            norm_lxp2 = abs(lxprod1 / (math.sqrt(sqr(h_l.x) + sqr(h_l.z)) + math.sqrt(sqr(hrd_l.x) + sqr(hrd_l.z))))
            rxprod2 = (h_r.x * hrd_r.z) - (h_r.z * hrd_r.x)
            # Note:  Lisp code below has lxprod1 instead of rxprod1
            norm_rxp2 = abs(rxprod1 / (math.sqrt(sqr(h_r.x) + sqr(h_r.z)) + math.sqrt(sqr(hrd_r.x) + sqr(hrd_r.z))))

            if(sign(lxprod1) != sign(lxprod2)):
                turn = 1
                go_on = False

            if(sign(rxprod1) != sign(rxprod2)):
                turn = 2
                go_on = False
            
            lxprod1 = lxprod2
            norm_lxp1 = norm_lxp2
            rxprod1 = rxprod2
            norm_rxp1 = norm_rxp2

            if(j >= (fracNearestRP + aheadMax)):
                turn = 0
                go_on = False
            
            if(j <= (fracNearestRP + aheadMin)):
                j = long(fracNearestRP + aheadMin)

            if(lane != 0):
                if(turn == 1): # left
                    fi = ((norm_lxp1 * (j-1)) + (norm_lxp2 * (j-2))) / (norm_lxp1 + norm_lxp2)
                    fpText = "ltp"
                    fpTPfracIndex = fi
                    return (left(fi, lane))
                elif(turn == 2): # right
                    fi = ((norm_rxp1 * (j-1)) + (norm_rxp2 * (j-2))) / (norm_rxp1 + norm_rxp2)
                    fpText = "rtp"
                    fpTPfracIndex = fi
                    return(right(fi, lane))
                else:
                    fi = fracNearestRP + aheadMax
                    fpText = "vp"
                    fpTPfracIndex = 0
                    return (middle(fi, lane))
            else:
                # Not implemented:  Only for lane changes
            
        return None

    distAhead = 400

    # Need to look into Graphics()
    def draw(self, g = Graphics(), env = Env()):
        long ri = env.simcar.roadIndex;

        # Look into how to set color, Polygon() function, and world2image in env
		g.setColor (Color.darkGray)
		Polygon p = new Polygon ()
		Coordinate newLoc = env.world2image (location (ri+3, 1))
		if (newLoc==null) return
		p.addPoint (newLoc.x, newLoc.y)
		newLoc = env.world2image (location (ri+distAhead, 1))
		p.addPoint (newLoc.x, newLoc.y)
		newLoc = env.world2image (location (ri+distAhead, 4))
		p.addPoint (newLoc.x, newLoc.y)
		newLoc = env.world2image (location (ri+3, 4))
		p.addPoint (newLoc.x, newLoc.y)
		g.fillPolygon (p)

        di = long(3)
        lps = [1, 2, 3, 4]
        oldLocs = Coordiante([None, None, None, None])
        while(di <= distAhead):
            g.setColor(Color.white)
            for(i in range (0, 4)):
                lp = lps[i]
                oldLoc = Coordinate(oldLocs[i])
                newLoc = env.world2image(location(ri+di, lp))
                if(((oldLoc != None) and (newLoc != None)) and ((lp == 1) or (lp == 4) or ((ri+di) % 5 < 2))):
                    oldLocs[i] = newLoc
                
                if(di < 50):
                    di = di + 1
                elif(di < 100):
                    di = di + 3
                else:
                    di = di + 25

        


    
