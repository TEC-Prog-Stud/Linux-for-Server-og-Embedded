import magnetic_compas
#from src.magnetic_compas import *

import unittest

## UnitTest af klassen MagneticCompas
class TestMagneticCompasUnit(unittest.TestCase):

    ## Tester at vi kan oprette en instans af MagneticCompas
    def test_construct(self):
        # Arrange
        
        # Act
        magcomp = magnetic_compas.MagneticCompas();
        # Assert
        self.assertIsInstance(magcomp, magnetic_compas.MagneticCompas)


        # Arrange
        # Act
        # Assert


#class TestMagneticCompasIntegration(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()