from userStory08 import us08_birth_b4_marr_parents
import unittest 

class UserStory08Test(unittest.TestCase):

    def test_us_08(self):
       error_list = us08_birth_b4_marr_parents("us08testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: FAMILY: US08: I19: born 1981-02-13 before marriage on 1981-02-14',
       'ERROR: FAMILY: US08: I26: born 1984-12-14 after divorce on 1981-02-14'])

        
        
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     