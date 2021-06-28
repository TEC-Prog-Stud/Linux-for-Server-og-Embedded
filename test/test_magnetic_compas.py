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
        # Act
        # Assert
        None

    def test_currentpixel_at_start(self):
        # Arrange
        magcomp = MagneticCompas();
        
        # Act
        # Assert
        self.assertTrue(False)

        None

        # Arrange
        # Act
        # Assert


#class TestMagneticCompasIntegration(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()