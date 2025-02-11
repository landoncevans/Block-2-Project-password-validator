import re

def isValid(password: str) -> bool:
    rules = r"^(?=.*[A-Z])(?=.*!).*$"
    if re.match(rules):
        True
    else:
        False