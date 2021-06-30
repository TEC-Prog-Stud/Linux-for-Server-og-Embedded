import math

class MagneticCompas():



    def __init__(self):
        self.currentPixelX = None
        self.currentPixelY = None
        self.__previousPixelX = None
        self.__previousPixelY = None

    def setCurrentPixel(self, x, y):
        self.previousPixelX = self.currentPixelX
        self.previousPixelY = self.currentPixelY
        self.currentPixelX = x
        self.currentPixelY = y

    def hNorth2rEast(deg):
        if deg > 90:
            return 2*math.pi - (deg-90)/360 * 2*math.pi
        else:
            return - (deg-90)/360 * 2*math.pi

    
    # def r2d(d):
    #     if d > 90:
    #         return 2*math.pi - (d-90)/360 * 2*math.pi
    #     else:
    #         return - (d-90)/360 * 2*math.pi