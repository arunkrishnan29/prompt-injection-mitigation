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

import re

INJECTION_PATTERNS = [
    r"ignore\s+previous\s+instructions",
    r"disregard\s+the\s+system\s+prompt",
    r"reveal\s+the\s+system\s+prompt",
    r"bypass\s+security",
]

def check_rules(prompt):
    cleaned_prompt = prompt.lower()
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, cleaned_prompt):
            return True
    return False