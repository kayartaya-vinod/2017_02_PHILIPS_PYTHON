import unittest
import dateutils as du

class TestMax_days_in_year(unittest.TestCase):

    def setUp(self):
        print("From within the self.setUp()")

    def tearDown(self):
        print("From within the self.tearDown()")

    def test_max_days_in_year(self):
        print("From within the test_max_days_in_year()")
        self.assertEquals(365, du.max_days_in_year(2017))
        self.assertEquals(366, du.max_days_in_year(2016))
        self.assertEquals(365, du.max_days_in_year(1900))

    def test_is_leap(self):
        print("From within the test_is_leap()")
        self.assertTrue(du.is_leap(2016))
        self.assertFalse(du.is_leap(2021))

if __name__ == '__main__':
    unittest.main()