# sanitizer.py

from rules import INJECTION_PATTERNS


def sanitize_prompt(prompt):
    """
    Remove dangerous prompt injection patterns
    """

    sanitized_prompt = prompt

    for pattern in INJECTION_PATTERNS:
        sanitized_prompt = sanitized_prompt.replace(pattern, "")

    return sanitized_prompt.strip()