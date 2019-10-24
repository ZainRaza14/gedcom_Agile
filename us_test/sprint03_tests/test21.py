from userstories.sprint03_us.userStory21 import us21_husb_male_wife_female
import unittest 

class UserStory21Test(unittest.TestCase):

    def test_us_21(self):
       error_list = us21_husb_male_wife_female("gedfilestest/sprint03_ged/us21testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: FAMILY: US21 : Husband Id:I01,name:Joe /Smith/ is not male', 
       'ERROR: FAMILY: US21 : Wife Id:I07,name:Jennifer /Smith/ is not female'])
     
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     
