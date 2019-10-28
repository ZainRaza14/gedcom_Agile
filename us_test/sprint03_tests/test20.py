from userstories.sprint03_us.userStory20 import us20_aunts_and_uncles

import unittest 

class UserStory20Test(unittest.TestCase):

    def test_us20(self):
       error_list = us20_aunts_and_uncles("gedfilestest/sprint03_ged/us20testdata.ged")
       print(error_list)
       self.assertEqual(error_list,["ERROR: US20 : I03 is married to their nephew or niece"])
     
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     
