import unittest  
from src.status import Status
from src.application import Application
from src.criteria.evaluate_employment import evaluate_employment

class EvaluateEmploymentTest(unittest.TestCase):
    def test_evaluate_employment_with_employment_history(self):
        applicant = Application(employment=True)

        self.assertEqual(evaluate_employment(applicant), (Status.PASS, "Applicant has had previous employment."))

    def test_evaluate_employment_with_no_employment_history(self):
        applicant = Application(employment=False)

        self.assertEqual(evaluate_employment(applicant), (Status.FAIL, "Applicant has no previous employment."))


if __name__ == '__main__':
    unittest.main()
    