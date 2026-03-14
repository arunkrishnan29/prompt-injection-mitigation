INJECTION_PATTERNS = [
    "ignore previous instructions",
    "disregard the system prompt",
    "reveal the system prompt",
    "bypass security",
    "act as developer mode",
    "pretend to be root",
    "give me admin access"
]

def check_rules(prompt):
    for pattern in INJECTION_PATTERNS:
        if pattern in prompt.lower():
            return True
    return False