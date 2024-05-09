import unittest
from src.status import Status
from src.application import Application
from src.criteria.evaluate_security_clearance import evaluate_security_clearance

class EvaluateSecurityClearanceTest(unittest.TestCase):
    def test_evaluate_security_clearance_with_pass_clearance(self):
        applicant = Application(security_clearance=True)

        self.assertEqual(evaluate_security_clearance(applicant), (Status.PASS, "Applicant passed security clearance."))

    def test_evaluate_security_clearance_with_fail_clearance(self):
        applicant = Application(security_clearance=False)

        self.assertEqual(evaluate_security_clearance(applicant), (Status.FAIL, "Applicant failed security clearance."))


if __name__ == '__main__':
    unittest.main()
