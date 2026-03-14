import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def print_banner():
    print("\n==============================")
    print("Prompt Injection Mitigation System")
    print("==============================\n")