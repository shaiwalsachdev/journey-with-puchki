
import re

def redact_text(text: str, is_private_mode: bool) -> str:
    if is_private_mode and text:
        # Redact sensitive words
        sensitive_words = ["kiss", "hugs", "hinge", "cheek pecks", "lips", "cuddle", "snuggle"]
        redacted_text = text
        for word in sensitive_words:
            # Replicating the logic from main.py
            pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
            redacted_text = pattern.sub("✨" * len(word), redacted_text)
        return redacted_text
    return text

# Test case
text = "Lots of cute hair clips for you"
redacted = redact_text(text, True)
print(f"Original: {text}")
print(f"Redacted: {redacted}")

# Check specifically for 'lips' in 'clips'
match = re.search(r'\blips\b', 'clips', re.IGNORECASE)
print(f"Does 'lips' match inside 'clips'? {match is not None}")
