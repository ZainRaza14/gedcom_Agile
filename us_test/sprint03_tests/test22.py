# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 01:05:28 2019

@author: NEIL
"""

from userstories.sprint03_us.userStory22 import us22_unique_IDs
import unittest 

class UserStory22Test(unittest.TestCase):

    def test_us22(self):
       error_list = us22_unique_IDs("gedfilestest/sprint03_ged/us22testdata.ged")
       print(error_list)
       self.assertEqual(error_list,["ERROR: US22 : The ids:['I01', 'F23'] are repeated"])
     
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)     
