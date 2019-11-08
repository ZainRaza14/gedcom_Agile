from userstories.sprint04_us.userStory28 import us28_order_sibilings_by_age
import unittest 

class UserStory28Test(unittest.TestCase):

    def test_us28(self):
       error_list = us28_order_sibilings_by_age("gedfilestest/sprint04_ged/us28testdata.ged")    
       print(error_list)
       self.assertEqual(error_list,["US28: The list of sibilings in sorting order according to their age are ['I898', 'I229', 'I226', 'I300']"])
    
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     
