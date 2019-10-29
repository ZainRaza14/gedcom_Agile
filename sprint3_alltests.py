import unittest
from us_test.sprint03_tests.test18 import UserStory18Test
from us_test.sprint03_tests.test19 import UserStory19Test
from us_test.sprint03_tests.test21 import UserStory21Test
from us_test.sprint03_tests.test22 import UserStory22Test
from us_test.sprint03_tests.test20 import UserStory20Test
from us_test.sprint03_tests.test24 import UserStory24Test


class Sprint03_Test(unittest.TestCase):
    UserStory18Test()
    UserStory19Test()
    UserStory21Test()
    UserStory22Test()
    UserStory24Test()
    
    
    

if __name__ == "__main__":
    unittest.main()
