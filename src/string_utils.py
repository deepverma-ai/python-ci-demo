def reverse_string(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1]


def is_palindrome(s: str) -> bool:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def capitalize_words(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return " ".join(word.capitalize() for word in s.split())


def count_vowels(s: str) -> int:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)
