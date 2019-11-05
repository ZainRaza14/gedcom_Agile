import unittest
from us_test.sprint04_tests.test27 import UserStory27Test
from us_test.sprint04_tests.test28 import UserStory28Test
from us_test.sprint04_tests.test30 import UserStory30Test
from us_test.sprint04_tests.test36 import UserStory36Test


class Sprint03_Test(unittest.TestCase):
    UserStory27Test()
    UserStory28Test()
    UserStory30Test()
    UserStory36Test()
    
    

if __name__ == "__main__":
    unittest.main()
