from userstories.sprint04_us.userStory28 import us28_order_sibilings_by_age
import unittest 

class UserStory28Test(unittest.TestCase):

    def test_us28(self):
       famDict = us28_order_sibilings_by_age("gedfilestest/sprint04_ged/us28testdata.ged")    
       self.assertEqual(famDict['F223'].multChild,['I898', 'I229', 'I226', 'I300'])
    
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     
