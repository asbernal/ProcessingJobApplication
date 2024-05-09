import unittest
from src.process_application import *
from src.application import Application
from src.criteria.evaluate_employment import evaluate_employment

class ProcessApplicationTest(unittest.TestCase):
    def canary_test(self):
        self.assertTrue(True)
    
    def test_process_application_with_no_criteria(self):
        applicant = Application()
    
        self.assertEqual(process_application(applicant), (Status.PASS, "Nothing to check"))

    def test_process_application_with_employment_history(self): 
        applicant = Application()
        employment_check = lambda applicant: (Status.PASS, "Applicant has had previous employment.") 

        self.assertEqual(process_application(applicant, employment_check), (Status.PASS, "Applicant has had previous employment."))

    def test_process_application_with_no_employment_history(self):
        applicant = Application()
        employment_check = lambda applicant: (Status.FAIL, "Applicant has no previous employment.")

        self.assertEqual(process_application(applicant, employment_check), (Status.FAIL, "Applicant has no previous employment."))

    def test_process_application_with_employment_history_and_no_criminal_record(self):
        applicant = Application()

        employment_check = lambda applicant: (Status.PASS, "Applicant has had previous employment.")
        criminal_record_check  = lambda applicant: (Status.PASS, "Applicant has had no criminal records.")

        result = process_application(applicant, employment_check, criminal_record_check)
        self.assertEqual(result, (Status.PASS, "Applicant has had previous employment. Applicant has had no criminal records."))
    
    def test_process_application_with_no_employment_and_no_criminal_record(self):
        applicant = Application()

        employment_check = lambda applicant: (Status.FAIL, "Applicant has no previous employment.")
        criminal_record_check = lambda applicant: (Status.PASS, "Applicant has had no criminal records.")

        result = process_application(applicant, employment_check, criminal_record_check)

        self.assertEqual(result, (Status.FAIL, "Applicant has no previous employment. Applicant has had no criminal records."))
    
    def test_process_application_with_employment_history_and_criminal_record(self):
        applicant = Application()

        employment_check = lambda applicant: (Status.PASS, "Applicant has had previous employment.")
        criminal_record_check = lambda applicant: (Status.FAIL, "Applicant has had criminal records.")

        result = process_application(applicant, employment_check, criminal_record_check)

        self.assertEqual(result, (Status.FAIL, "Applicant has had previous employment. Applicant has had criminal records."))


if __name__ == '__main__':
    unittest.main()
