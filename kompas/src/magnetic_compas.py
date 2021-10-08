import math

class MagneticCompas():



    def __init__(self):
        pass

    def hNorth2rEast(deg):
        """
            Calculate the 360 deg bearing from north, clockwize, to radians from first axis, counterclockwize
        """
        ## when the compas is in the 2nd, 3rd or 4th qadrant (90-360 deg or east to north clockwice (3-o-clock to 12 o-clock))
        ## we take substract the radians from a whole round (2*pi)
        if deg > 90:
            return 2*math.pi - math.radians(deg-90) 
        else:
            return - math.radians(deg-90)
