import src.magnetic_compas
from src.magnetic_compas import *

import unittest

## UnitTest af klassen MagneticCompas
class TestMagneticCompasUnit(unittest.TestCase):

    ## Tester at vi kan oprette en instans af MagneticCompas
    def test_construct(self):
        # Arrange
        
        # Act
        magcomp = MagneticCompas();
        # Assert
        self.assertIsInstance(magcomp, MagneticCompas)

    def test_rad2East(self):
        # Arrange
        magcomp = MagneticCompas();
        
        # Act
        north = MagneticCompas.hNorth2rEast( 0 )
        east  = MagneticCompas.hNorth2rEast( 90 ) 
        south = MagneticCompas.hNorth2rEast( 180 )
        west  = MagneticCompas.hNorth2rEast( 270 )

        ne    = MagneticCompas.hNorth2rEast( 45 )

        # Assert
        self.assertEquals(north, 0.5*math.pi, "north")
        self.assertEquals(east,  0.0*math.pi, "east")
        self.assertEquals(south, 1.5*math.pi, "south")
        self.assertEquals(west,  1.0*math.pi, "west")

        self.assertEquals(ne,    .25*math.pi, "ne")
        


        # Arrange
        # Act
        # Assert


if __name__ == '__main__':
    unittest.main()