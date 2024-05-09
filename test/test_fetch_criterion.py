import unittest
from src.status import Status
from src.fetch_criterion import fetch_criterion
from src.criteria.evaluate_employment import evaluate_employment
from src.criteria.evaluate_criminal_record import evaluate_criminal_record


class FetchCriterionTest(unittest.TestCase):
    def test_fetch_criterion_with_employment_criteria(self):
        criterion = fetch_criterion("employment")

        self.assertEqual(criterion, evaluate_employment)
    
    def test_fetch_criterion_with_criminal_record_criteria(self):
        criterion = fetch_criterion("criminal record")

        self.assertEqual(criterion, evaluate_criminal_record)

if __name__ == '__main__':
    unittest.main()
