from src.status import Status

def evaluate_credit_record(applicant):
    return (Status.PASS, "Applicant has good credit.") if applicant.credit_record \
            else (Status.FAIL, "Applicant has bad credit.")
