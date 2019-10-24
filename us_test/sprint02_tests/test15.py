from userstories.sprint02_us.userStory15 import us15_fewer_than_15_siblings
import unittest 

class UserStory15Test(unittest.TestCase):

    def test_us15(self):
        
       error_list = us15_fewer_than_15_siblings("gedfilestest/sprint02_ged/us15testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: FAMILY: US15: Family has more than 15 siblings F45'])     
       
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)  