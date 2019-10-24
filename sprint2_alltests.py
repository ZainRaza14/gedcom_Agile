import unittest
from us_test.sprint02_tests.test09 import UserStory09Test
from us_test.sprint02_tests.test16 import UserStory16Test
from us_test.sprint02_tests.test10 import UserStory10Test
from us_test.sprint02_tests.test11 import UserStory11Test
from us_test.sprint02_tests.test12 import UserStory12Test
from us_test.sprint02_tests.test13 import UserStory13Test
from us_test.sprint02_tests.test14 import UserStory14Test
from us_test.sprint02_tests.test15 import UserStory15Test


class Sprint02_Test(unittest.TestCase):
    UserStory09Test()
    UserStory10Test()
    UserStory11Test()
    UserStory12Test()
    UserStory13Test()
    UserStory14Test()
    UserStory15Test()
    UserStory16Test()
    

if __name__ == "__main__":
    unittest.main()
