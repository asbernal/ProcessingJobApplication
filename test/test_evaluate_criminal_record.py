import unittest
from src.status import Status
from src.application import Application
from src.criteria.evaluate_criminal_record import evaluate_criminal_record

class EvaluateCriminalRecordTest(unittest.TestCase):
    def test_evaluate_criminal_record_with_having_criminal_record(self):
        applicant = Application(criminal_record=True)

        self.assertEqual(evaluate_criminal_record(applicant), (Status.FAIL, "Applicant has had criminal records."))

    def test_evaluate_criminal_record_with_no_criminal_record(self):
        applicant = Application(criminal_record=False)

        self.assertEqual(evaluate_criminal_record(applicant), (Status.PASS, "Applicant has had no criminal records."))


if __name__ == '__main__':
    unittest.main()
    