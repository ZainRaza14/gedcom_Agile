from userstories.sprint02_us.userStory14 import us14_multiple_births
import unittest 

class UserStory14Test(unittest.TestCase):

    def test_us14(self):
        
       error_list = us14_multiple_births("gedfilestest/sprint02_ged/us14testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: FAMILY: US14 Family F23 has more than 5 siblings born at the same time'])        
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     