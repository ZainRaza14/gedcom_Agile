from userstories.sprint02_us.userStory10 import us10_marr_after_14
import unittest 

class UserStory10Test(unittest.TestCase):

    def test_us10(self):
        
       error_list = us10_marr_after_14("gedfilestest/sprint02_ged/us10testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: US10 - The individual I01 was married before 14, this is not valid']) 
              
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)  