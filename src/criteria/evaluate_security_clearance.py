from src.status import Status

def evaluate_security_clearance(applicant):
    return (Status.PASS, "Applicant passed security clearance.") if applicant.security_clearance \
            else (Status.FAIL, "Applicant failed security clearance.")
