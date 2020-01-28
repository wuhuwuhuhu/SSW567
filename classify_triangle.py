"""
This script is used to solve triangle assignment and autotest
By Haodong Wu 01/27/2020
"""
import unittest
def classifyTriangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
    """
    try:
        side1 = float(a)
    except ValueError:
        print(f'{a}is not a number')
        return "NotATriangle"
    try:
        side2 = float(b)
    except ValueError:
        print(f'{b}is not a number')
        return "NotATriangle"

    try:
        side3 = float(c)
    except ValueError:
        print(f'{c}is not a number')
        return "NotATriangle"
    [side1,side2,side3].sort
    #make side list sequentially
    if (side1 == side2 and side1 == side3):
        return "Equilateral"
    elif (side1 + side2 > side3 and (side1 == side2 or side1 == side3 or side2 == side3)):
        return "Isoceles"
    elif (side1**2 + side2**2 == side3**2):
        return "Right"
    elif(side1 + side2 > side3):
        return "Scalene"
    else:
        return "NotATriangle"

    
class TestFraction(unittest.TestCase):
    def test_classifyTriangle(self):
        self.assertEqual(classifyTriangle('a',1,2),"NotATriangle")
        self.assertEqual(classifyTriangle(1,1,1),"Equilateral")
        self.assertEqual(classifyTriangle(2,2,3),"Isoceles")
        self.assertEqual(classifyTriangle(1,1,2),"NotATriangle")
        self.assertEqual(classifyTriangle(3,4,5),"Right")
        self.assertEqual(classifyTriangle(3,4,5.5),"Scalene")
        self.assertEqual(classifyTriangle(1,4,5),"NotATriangle")

if __name__ == "__main__":
    unittest.main(exit=False,verbosity=2)
    