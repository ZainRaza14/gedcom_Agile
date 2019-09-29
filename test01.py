from userStory01 import us01_dates_b4_curr_date
import unittest 

class UserStory01Test(unittest.TestCase):

    def test_us01(self):
        
       error_list = us01_dates_b4_curr_date("us01testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: INDIVIDUAL: US01: I01: Birthday 2020-07-15 is after todays date',
        'ERROR: INDIVIDUAL: US01: I01: Death Date 2021-12-31 is after todays date', 
        'ERROR: FAMILY: US01: F23: Marriage Date 2020-09-29  is after todays date', 
        'ERROR: FAMILY: US01: F23: Divorce Date 2021-12-14  is after todays date'])

        
        
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     