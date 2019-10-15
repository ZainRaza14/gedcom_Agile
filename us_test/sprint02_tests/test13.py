from userstories.sprint02_us.userStory13 import us13_siblings_spacing
import unittest 

class UserStory13Test(unittest.TestCase):
    def test_us13(self):
        
       error_list = us13_siblings_spacing("gedfilestest/sprint02_ged/us13testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: FAMILY: US13: The spacing between sibling1:I19 and sibling2:I26 of family:F23 is not valid',
                                    'ERROR: FAMILY: US13: The spacing between sibling1:I27 and sibling2:I19 of family:F23 is not valid',
                                    'ERROR: FAMILY: US13: The spacing between sibling1:I27 and sibling2:I26 of family:F23 is not valid'])        

    if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     
