import unittest
from employee import Employee

class test_employee(unittest.TestCase):

    '''instead of having to create the same Bob emp1 and Alice emp2 object for each method, 
    we can use "setUp()" and "tearDown()" methods
    '''

    #The code in here will run b4 every single test
    def setUp(self):
        #we have to store these employees as attributes of self
        #and if we want to refer to it later, we have to write "self." and then the attribute name
        self.emp1 = Employee("Bob", "Adams", 10000)
        self.emp2 = Employee("Alice", "Smith", 15000)

    #The code in here will run after every single test
    def tearDown(self):
        pass

    def test_email(self):

        self.assertEquals(self.emp1.email, "Bob.Adams@gmail.com")
        self.assertEquals(self.emp2.email, "Alice.Smith@gmail.com")

        self.emp1.first = "Brad"
        self.emp2.first = "Anne"

        self.assertEquals(self.emp1.email, "Brad.Adams@gmail.com")
        self.assertEquals(self.emp2.email, "Anne.Smith@gmail.com")

    def test_full_name(self):
        self.assertEquals(self.emp1.fullname, "Bob Adams")
        self.assertEquals(self.emp2.fullname, "Alice Smith")

        self.emp1.first = "Brad"

    #Go through mocking tests later if you have time
    #Very useful for testing code that uses networking resources

if __name__ == "__main__":
    unittest.main()


