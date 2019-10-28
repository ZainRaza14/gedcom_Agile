from userstories.sprint03_us.userStory18 import us18_sibilings_no_marriage
import unittest 

class UserStory18Test(unittest.TestCase):

    def test_us18(self):
       error_list = us18_sibilings_no_marriage("gedfilestest/sprint03_ged/us18testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: FAMILY: US18 : Sibiings Id:I26,name:Jane /Smith/ and  Id:I19,name:Dick /Smith/ are married'])
    
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     
