from userstories.sprint04_us.userStory27 import us27_individual_ages
import unittest 

class UserStory27Test(unittest.TestCase):

    def test_us27(self):
       error_list = us27_individual_ages("gedfilestest/sprint04_ged/us27testdata.ged")
       print(error_list)
       self.assertEqual(error_list,["US27: The list of individuals along with their ages are:{'I01': 53, 'I07': 59, 'I19': 38, 'I26': 36}"])

     
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     
