from userstories.sprint04_us.userStory35 import us35_list_recent_births
import unittest 

class UserStory35Test(unittest.TestCase):

    def test_us35(self):
       error_list = us35_list_recent_births("gedfilestest/sprint04_ged/us35testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: INDIVIDUAL: US35: The individual I02 was born within the last 30 days'])

     
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     
