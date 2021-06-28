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

    def test_setCurrentPixel(self):
        # Arrange
        magcomp = MagneticCompas();
        # Act
        magcomp.setCurrentPixel(1,2)
        # Assert
        self.assertEqual(magcomp.currentPixelX, 1)
        self.assertEqual(magcomp.currentPixelY, 2)

    def test_currentpixel_at_start(self):
        # Arrange
        magcomp = MagneticCompas();
        
        # Act
        # Assert
        self.assertEqual(magcomp.currentPixelX, None)
        self.assertEqual(magcomp.currentPixelY, None)



        # Arrange
        # Act
        # Assert


if __name__ == '__main__':
    unittest.main()