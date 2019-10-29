from userstories.sprint03_us.userStory23 import us23_unique_name_and_birth
import unittest 

class UserStory23Test(unittest.TestCase):

    def test_us(self):
       error_list = us23_unique_name_and_birth("gedfilestest/sprint03_ged/us23testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: INDIVIDUAL: US23: No more than one individual with the same name and birth date should appear in GEDCOM file',
                                    'ERROR: INDIVIDUAL: US23: No more than one individual with the same name and birth date should appear in GEDCOM file'])
    
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     