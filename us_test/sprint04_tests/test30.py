from userstories.sprint04_us.userStory30 import us30_list_living_married
import unittest 

class UserStory30Test(unittest.TestCase):

    def test_us30(self):
       error_list = us30_list_living_married("gedfilestest/sprint04_ged/us30testdata.ged")
       print(error_list)
       self.assertTrue(error_list,"US30: The list of individuals along with their ages are:dict_keys(['I2122', 'I1171'])")
     
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     
