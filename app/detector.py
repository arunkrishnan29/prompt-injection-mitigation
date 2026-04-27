

# #* detector.py
# ##py
from rules import check_rules


class PromptInjectionDetector:

    def __init__(self):
        pass

    def detect(self, prompt):
        """
        Detect prompt injection using rule patterns
        """

        rule_result = check_rules(prompt)

        if rule_result:
            return True
        else:
            return False

