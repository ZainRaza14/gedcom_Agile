from userstories.sprint02_us.userStory16 import us16_male_last_names
import unittest 

class UserStory16Test(unittest.TestCase):

    def test_us_16(self):
        
       error_list = us16_male_last_names("gedfilestest/sprint02_ged/us16testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: FAMILY: US16: Individual I29 Name: Robbie /Jack/ not matched with family first name: Smith'])
       print("working")
     
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     
