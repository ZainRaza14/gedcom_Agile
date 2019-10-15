from userstories.sprint02_us.userStory09 import us09_birth_b4_parents_death
import unittest 

class UserStory09Test(unittest.TestCase):

    def test_us_09(self):
        
       error_list = us09_birth_b4_parents_death("gedfilestest/sprint02_ged/us09testdata.ged")
       print(error_list)
       self.assertEqual(error_list,[
           'ERROR: FAMILY: US09 : Individual I19 Name: Dick adom /Smith/ born after death of mother I07 Jennifer /Smith/',
           'ERROR: FAMILY: US09 : Individual I19 Name: Dick adom /Smith/ born 9 months after death of father I01 Joe /Smith/',
           'ERROR: FAMILY: US09 : Individual I26 Name: Jane bdom /Smith/ born 9 months after death of father I01 Joe /Smith/'
           ])
    
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     
