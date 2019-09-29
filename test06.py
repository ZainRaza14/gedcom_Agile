from userStory06 import us06_divo_b4_death
import unittest 

class UserStory06Test(unittest.TestCase):

    def test_us06(self):
        
       error_list = us06_divo_b4_death("us06testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: FAMILY: US06: F23 : Divorce 1999-02-14 is after death 1998-12-31'])

        
        
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     