#Also IMPORTANT: the file with our tests must start with "test_"

#unittest is basically like JUNIT
import unittest
#import the file we are testing on
import unit_testing_practise


'''Tests advice:
Put tests that cover edge cases. 
If we later find a bug, that our tests didn't catch, we should add a test case to catch this bug now
'''


#create a class with an arbitrary name, and make sure it inherits from unittest.TestCase
class TestUnitTesting(unittest.TestCase):
    
    #we must define a method, and the method must start with "test_"
    def test_add(self):
        result = unit_testing_practise.add(10,5)
        self.assertEquals(result, 15)

    def test_sub(self):
        result = unit_testing_practise.subtract(20, 8)
        self.assertEquals(result, 12)

    def test_mul(self):
        result = unit_testing_practise.multiply(23, 6)
        self.assertEquals(result, 138)

    def test_div(self):
        result = unit_testing_practise.divide(20,4)
        self.assertEquals(result, 5)

        #testing whether an exception has been "raised"
        #format is (Type of exception, name of function without (), arg 1, arg 2, etc)
        self.assertRaises(ValueError, unit_testing_practise.divide, 10, 0)

        #alternative to above is using a context manager
        with self.assertRaises(ValueError):
            unit_testing_practise.divide(10,0)

    
#This allows us to run all of our tests 
#Click on the chemical flask in the left side bar to see the results of the unit testing in the GUI
#Make sure to click the Run arrow button
if __name__ == "__main__":
    unittest.main()
