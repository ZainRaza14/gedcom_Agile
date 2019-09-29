from userStory03 import us03_birth_b4_death
import unittest 

class UserStory03Test(unittest.TestCase):

    def test_us03(self):
        
       error_list = us03_birth_b4_death("us03testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: INDIVIDUAL: US03: I01 : Died 1959-12-31 before born 1960-07-15'])

        
        
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     