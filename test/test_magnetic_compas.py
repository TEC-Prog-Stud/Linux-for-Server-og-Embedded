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
        north = magcomp.radToEast( 0 )
        east  = magcomp.radToEast( 90 ) 
        south = magcomp.radToEast( 180 )
        west  = magcomp.radToEast( 270 )

        ne    = magcomp.radToEast( 45 )

        # Assert
        self.assertEquals(north, 0.5*math.pi, "north")
        self.assertEquals(east,  0.0*math.pi, "east")
        self.assertEquals(south, 1.5*math.pi, "south")
        self.assertEquals(west,  1.0*math.pi, "west")

        self.assertEquals(ne,    .25*math.pi, "ne")
        


    # def test_setCurrentPixel(self):
    #     # Arrange
    #     magcomp = MagneticCompas();
    #     # Act
    #     magcomp.setCurrentPixel(1,2)
    #     # Assert
    #     self.assertEqual(magcomp.currentPixelX, 1)
    #     self.assertEqual(magcomp.currentPixelY, 2)

    # def test_currentpixel_at_start(self):
    #     # Arrange
    #     magcomp = MagneticCompas();
    #     # Act
    #     pass
    #     # Assert
    #     self.assertEqual(magcomp.currentPixelX, None)
    #     self.assertEqual(magcomp.currentPixelY, None)

    # def test_prevpixel_hidden(self):
    #     # Arrange
    #     magcomp = MagneticCompas();
    #     # Act
    #     # Assert
    #     with self.assertRaises(AttributeError) as raisedException:
    #         print(magcomp.__previousPixelX)
    #     with self.assertRaises(AttributeError) as raisedException:
    #         print(magcomp.__previousPixelY)

    #     #magcomp.__previousPixelX = 0

    #     #with self.assertRaises(AttributeError) as raisedException:
    #     # with self.assertRaises(BaseException) as raisedException:
    #     #     magcomp.__previousPixelX = 42
    #     # print('raisedException:', raisedException)



        # Arrange
        # Act
        # Assert


if __name__ == '__main__':
    unittest.main()