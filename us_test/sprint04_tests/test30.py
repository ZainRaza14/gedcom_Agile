from userstories.sprint04_us.userStory30 import us30_list_living_married
import unittest 

class UserStory30Test(unittest.TestCase):

    def test_us30(self):
       newindDict = us30_list_living_married("gedfilestest/sprint04_ged/us30testdata.ged")
       #print(newindDict)
       self.assertTrue('I2122' in newindDict)
     
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     
