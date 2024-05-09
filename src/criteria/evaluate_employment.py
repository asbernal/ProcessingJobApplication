from src.status import Status

def evaluate_employment(applicant):
    return (Status.PASS, "Applicant has had previous employment.") if applicant.employment else (Status.FAIL, "Applicant has no previous employment.")
