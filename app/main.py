# main.py

from detector import PromptInjectionDetector
from sanitizer import sanitize_prompt
from llm_interface import query_llm
from utils import print_banner


def main():

    print_banner()

    detector = PromptInjectionDetector()

    user_prompt = input("Enter your prompt: ")

    is_attack = detector.detect(user_prompt)

    if is_attack:
        print("\n⚠ Prompt Injection Detected!")

        safe_prompt = sanitize_prompt(user_prompt)

        print("Sanitized Prompt:", safe_prompt)

        response = query_llm(safe_prompt)

    else:
        response = query_llm(user_prompt)

    print("\nFinal LLM Response:")
    print(response)


if __name__ == "__main__":
    main()