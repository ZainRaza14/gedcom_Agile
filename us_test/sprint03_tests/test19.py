# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 03:59:52 2019

@author: NEIL
"""

from userstories.sprint03_us.userStory19 import us19_no_1st_cousin_marr
import unittest 

class UserStory19Test(unittest.TestCase):

    def test_us19(self):
       error_list = us19_no_1st_cousin_marr("gedfilestest/sprint03_ged/us19testdata.ged")
       print(error_list)
       self.assertEqual(error_list,['ERROR: FAMILY: US19: The two first cousins I49 and I33 cannot be married together'])
     
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     
