from dataclasses import dataclass

@dataclass
class Application:
    employment: bool = False
    criminal_record: bool = False
    credit_record: bool = False
    security_clearance: bool = False
