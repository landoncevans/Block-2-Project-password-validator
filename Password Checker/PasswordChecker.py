import re

def isValid(password: str) -> bool:
    rules = r"^(?=.*[A-Z])(?=.*!).*$"
    if re.match(rules, password) and  len(password) == 20:
        return True
    else:
        return False