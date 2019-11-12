from userstories.sprint04_us.userStory29 import us29_list_deceased
import unittest 

class UserStory29Test(unittest.TestCase):

    def test_us29(self):
       error_list = us29_list_deceased("gedfilestest/sprint04_ged/us29testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: INDIVIDUAL: US29: The individual I01 is dead',
                                    'ERROR: INDIVIDUAL: US29: The individual I02 is dead'])

if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)      
