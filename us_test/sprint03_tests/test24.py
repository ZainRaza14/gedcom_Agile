from userstories.sprint03_us.userStory24 import us24_unique_fam_by_spouses

import unittest 

class UserStory24Test(unittest.TestCase):

    def test_us24(self):
       error_list = us24_unique_fam_by_spouses("gedfilestest/sprint03_ged/us24testdata.ged")
       print(error_list)
       self.assertEqual(error_list,["ERROR: US24 : husband, wife names or marriage date is occurring twice in Gedcom ", 
                                    "ERROR: US24 : husband, wife names or marriage date is occurring twice in Gedcom ", 
                                    "ERROR: US24 : husband, wife names or marriage date is occurring twice in Gedcom "])
     
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     
