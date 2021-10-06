import math
#import src.magnetic_compas
from src.magnetic_compas import *

class DisplayCompas():

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

    def angle2pixels(self, angle):
        rad = MagneticCompas.hNorth2rEast(angle)
        x = math.ceil(math.cos(rad)*3.9) + 3
        y = math.ceil(math.sin(rad)*3.9) + 3
        return (x, y)

