from userStory08 import user_story08
import unittest 

class UserStory08Test(unittest.TestCase):

    def test_us_08(self):
       error_list = user_story08("us08testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ANOMALY: FAMILY: US08: I19: born 1981-02-13 before marriage on 1981-02-14',
       'ANOMALY: FAMILY: US08: I26: born 1984-12-14 after divorce on 1981-02-14'])

        
        
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     