import unittest
from us_test.sprint04_tests.test27 import UserStory27Test
from us_test.sprint04_tests.test28 import UserStory28Test
from us_test.sprint04_tests.test30 import UserStory30Test
from us_test.sprint04_tests.test36 import UserStory36Test
from us_test.sprint04_tests.test29 import UserStory29Test
from us_test.sprint04_tests.test31 import UserStory31Test
from us_test.sprint04_tests.test32 import UserStory32Test
from us_test.sprint04_tests.test35 import UserStory35Test


class Sprint03_Test(unittest.TestCase):
    UserStory27Test()
    UserStory28Test()
    UserStory29Test()
    UserStory30Test()
    UserStory31Test()
    UserStory32Test()
    UserStory35Test()
    UserStory36Test()
    
    

if __name__ == "__main__":
    unittest.main()
