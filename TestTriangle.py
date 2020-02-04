# -*- coding: utf-8 -*-
'''
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
'''

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testIsocelesTriangles(self): 
        self.assertEqual(classifyTriangle(2,2,3),'Isosceles','2,2,3 is a Isoceles triangle')
    
    def testNotATriangleTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,2),'NotATriangle','1,1,2 is not a triangle')
    
    def testNotATriangleTrianglesB(self):
        self.assertEqual(classifyTriangle(1,4,5),'NotATriangle','1,4,5 is not a triangle')

    def testScaleneTrianglesB(self):
        self.assertEqual(classifyTriangle(3,4,5.5),'Scalene','3,4,5.5 is a scalene triangle')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(200,300,400),'InvalidInput','200,300,400 are invalid input')

    def testInvalidInputB(self): 
        self.assertEqual(classifyTriangle(-1,1,2),'InvalidInput','-1,1,2 are invalid input')

    def testInvalidInputC(self): 
        self.assertEqual(classifyTriangle('a',1,2),'InvalidInput','a,1,2 are invalid input')

if __name__ == "__main__":
    print('Running unit tests')
    unittest.main()

