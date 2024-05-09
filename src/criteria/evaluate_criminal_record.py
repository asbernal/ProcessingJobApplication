from src.status import Status

def evaluate_criminal_record(applicant):
    return (Status.PASS, "Applicant has had no criminal records.") if not applicant.criminal_record  \
            else (Status.FAIL, "Applicant has had criminal records.")
