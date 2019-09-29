from userStory04 import user_story04
import unittest 

class UserStory04Test(unittest.TestCase):

    def test_us_04(self):
        
       error_list = user_story04("us04testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: FAMILY: US04: F23: Divorced 1980-03-14 before married 1981-02-14 '])

        
        
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     