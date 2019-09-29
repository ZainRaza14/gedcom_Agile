from userStory05 import us05_marr_b4_death
import unittest 

class UserStory05Test(unittest.TestCase):

    def test_us05(self):
        
       error_list = us05_marr_b4_death("us05testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: FAMILY: US05: F23 : Marriage of wife:I07 occurs after death',
        'ERROR: FAMILY: US05: F23 : Marriage of husband:I01 occurs after death'])

        
        
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     