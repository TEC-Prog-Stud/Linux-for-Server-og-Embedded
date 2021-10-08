import src.display_compas
from src.display_compas import *

import unittest

## UnitTest af klassen MagneticCompas
class TestDisplayCompasUnit(unittest.TestCase):

    ## Tester at vi kan oprette en instans af MagneticCompas
    def test_construct(self):
        # Arrange
        
        # Act
        displaycomp = DisplayCompas();
        # Assert
        self.assertIsInstance(displaycomp, DisplayCompas)

    def test_setCurrentPixel(self):
        # Arrange
        displaycomp = DisplayCompas();
        # Act
        displaycomp.setCurrentPixel(1,2)
        # Assert
        self.assertEqual(displaycomp.currentPixelX, 1)
        self.assertEqual(displaycomp.currentPixelY, 2)

    def test_currentpixel_at_start(self):
        # Arrange
        displaycomp = DisplayCompas();
        # Act
        pass
        # Assert
        self.assertEqual(displaycomp.currentPixelX, None)
        self.assertEqual(displaycomp.currentPixelY, None)

    def test_prevpixel_hidden(self):
        # Arrange
        displaycomp = DisplayCompas();
        # Act
        # Assert
        with self.assertRaises(AttributeError) as raisedException:
            print(displaycomp.__previousPixelX)
        with self.assertRaises(AttributeError) as raisedException:
            print(displaycomp.__previousPixelY)

        #displaycomp.__previousPixelX = 0

        #with self.assertRaises(AttributeError) as raisedException:
        # with self.assertRaises(BaseException) as raisedException:
        #     displaycomp.__previousPixelX = 42
        # print('raisedException:', raisedException)

    def test_angle2pixel_northeast(self):
        # Arrange
        displaycomp = DisplayCompas();
        
        # Act
        (x, y) = displaycomp.angle2pixels(45)
        
        # Assert
        self.assertEqual(x, 6)
        self.assertEquals(y, 6)

    def test_angle2pixel_north_northeast(self):
        # Arrange
        displaycomp = DisplayCompas();
        
        # Act
        (x, y) = displaycomp.angle2pixels(22.5)
        
        # Assert
        self.assertEqual(x, 5)
        self.assertEquals(y, 7)

    def test_angle2pixel_north_north_northeast(self):
        # Arrange
        displaycomp = DisplayCompas();
        
        # Act
        (x, y) = displaycomp.angle2pixels(11.25)
        
        # Assert
        self.assertEqual(x, 4)
        self.assertEquals(y, 7)

    def test_angle2pixel_eastsoutheast(self):
        # Arrange
        displaycomp = DisplayCompas();
        
        # Act
        (x, y) = displaycomp.angle2pixels(102.5)
        
        # Assert
        self.assertEqual(x, 7)
        self.assertEquals(y, 3)

    def test_angle2pixel_southwest(self):
        # Arrange
        displaycomp = DisplayCompas();
        
        # Act
        (x, y) = displaycomp.angle2pixels(225)
        
        # Assert
        self.assertEqual(x, 1)
        self.assertEquals(y, 1)

    def test_angle2pixel_north(self): 
        # Arrange
        displaycomp = DisplayCompas();
        
        # Act
        (x, y) = displaycomp.angle2pixels(0)
        
        # Assert
        self.assertEqual(x, 4)
        self.assertEquals(y, 7)

    def test_angle2pixel_west(self):
        # Arrange
        displaycomp = DisplayCompas();
        
        # Act
        (x, y) = displaycomp.angle2pixels(270)
        
        # Assert
        self.assertEqual(x, 0)
        self.assertEquals(y, 4)

    def test_angle2pixel_south(self):
        # Arrange
        displaycomp = DisplayCompas();
        
        # Act
        (x, y) = displaycomp.angle2pixels(180)
        
        # Assert
        self.assertEqual(x, 3)
        self.assertEquals(y, 0)



        # Arrange
        # Act
        # Assert


if __name__ == '__main__':
    unittest.main()