import unittest
from src.fetch_criteria import fetch_criteria
from src.application import Application

class FetchCriteriaTest(unittest.TestCase):
    def test_fetch_criteria_contains_employment(self):
        self.assertIn("employment", fetch_criteria())

    def test_fetch_criteria_contains_criminal_record(self):
        self.assertIn("criminal record", fetch_criteria())


if __name__ == '__main__':
    unittest.main()
