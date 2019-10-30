from userstories.sprint03_us.userStory17 import us17_no_marr_2_children
import unittest 

class UserStory17Test(unittest.TestCase):

    def test_us17(self):
       error_list = us17_no_marr_2_children("gedfilestest/sprint03_ged/us17testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: FAMILY: US17: F23 Parents should not marry their descendants'])
    
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     