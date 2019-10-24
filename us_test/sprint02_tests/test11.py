from userstories.sprint02_us.userStory11 import us11_no_bigamy
import unittest 

class UserStory11Test(unittest.TestCase):

    def test_us11(self):
        
       error_list = us11_no_bigamy("gedfilestest/sprint02_ged/us11testdata.ged")
       print(error_list)
       self.assertEqual(error_list,[
           'ERROR: INDIVIDUAL: US11: I01:Married2 F23 & F24',
           'ERROR: INDIVIDUAL: US11: I19:Married2 F25 & F26',
           'ERROR: INDIVIDUAL: US11: I29:Married2 F27 & F28'
           ])        
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     