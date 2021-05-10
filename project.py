from mathdojo import MathDojo
import unittest

# Write the add method and test it by calling it 3 times, with different numbers of arguments each time

class addTests(unittest.TestCase):    
    def testOne(self):
        md = MathDojo()
        self.assertEqual(md.add(2).result, 2)

    def testTwo(self):
        md = MathDojo()
        self.assertEqual(md.add(2, 2).result, 4)
    
    def testThree(self):
        md = MathDojo()
        self.assertEqual(md.add(2, 2, 2).result, 6)

    # def setUp(self):
    #     md = MathDojo()

    # def tearDown(self):
    #     print("running tearDown tasks for addTests")



# # Write the subtract method and test it by calling it 3 times, with different numbers of arguments each time
class subtractTests(unittest.TestCase):
    def testOne(self):
        md = MathDojo()
        self.assertEqual(md.subtract(2).result, -2)
    
    def testTwo(self):
        md = MathDojo()
        self.assertEqual(md.subtract(2, 2).result, -4)

    def testThree(self):
        md = MathDojo()
        self.assertEqual(md.subtract(2, 2, 2).result, -6)

    # def setUp(self):
    #     md = MathDojo()

    # def tearDown(self):
    #     print("running tearDown tasks for addTests")




# # Make sure you are able to chain methods as demonstrated above
class chainTests(unittest.TestCase):
    def testOne(self):
        md = MathDojo()
        self.assertEqual(md.add(2, 2, 2).subtract(2, 2, 2).result, 0)
    
    def testTwo(self):
        md = MathDojo()
        self.assertEqual(md.add(2).add(2, 5, 1).subtract(3, 2).result, 5)

    # def setUp(self):
    #     md = MathDojo()

    # def tearDown(self):
    #     print("running tearDown tasks for addTests")


if __name__ == '__main__':
    unittest.main()       