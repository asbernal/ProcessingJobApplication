import unittest
from src.status import Status
from src.application import Application
from src.criteria.evaluate_credit_record import evaluate_credit_record

class EvaluateCreditRecordTest(unittest.TestCase):
    def test_evaluate_credit_record_with_good_credit(self):
        applicant = Application(credit_record=True)

        self.assertEqual(evaluate_credit_record(applicant), (Status.PASS, "Applicant has good credit."))

    def test_evaluate_credit_record_with_bad_credit(self):
        applicant = Application(credit_record=False)

        self.assertEqual(evaluate_credit_record(applicant), (Status.FAIL, "Applicant has bad credit."))


if __name__ == '__main__':
    unittest.main()
