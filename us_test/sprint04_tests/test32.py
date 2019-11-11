from userstories.sprint04_us.userStory32 import us32_list_multiple_births
import unittest 

class UserStory32Test(unittest.TestCase):

    def test_us32(self):
       error_list = us32_list_multiple_births("gedfilestest/sprint04_ged/us32testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: INDIVIDUAL: US32: The individual I01 has multiple births','ERROR: INDIVIDUAL: US32: The individual I02 has multiple births'])

     
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     
