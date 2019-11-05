from userstories.sprint04_us.userStory36 import us36_list_recent_deaths
import unittest 

class UserStory36Test(unittest.TestCase):

    def test_us36(self):
       error_list = us36_list_recent_deaths("gedfilestest/sprint04_ged/us36testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: INDIVIDUAL: US36: The individual I01 died recently on 2019-11-05','ERROR: INDIVIDUAL: US36: The individual I07 died recently on 2019-11-04'])

     
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     
