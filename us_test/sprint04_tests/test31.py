from userstories.sprint04_us.userStory31 import us31_list_living_single
import unittest 

class UserStory31Test(unittest.TestCase):

    def test_us31(self):
       error_list = us31_list_living_single("gedfilestest/sprint04_ged/us31testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: INDIVIDUAL: US31: The individual I01 is single and above 30',])

if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     