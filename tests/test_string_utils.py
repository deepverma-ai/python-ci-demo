import pytest
from src.string_utils import reverse_string, is_palindrome, capitalize_words, count_vowels


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""


def test_reverse_string_invalid():
    with pytest.raises(TypeError):
        reverse_string(123)


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("RaceCar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("nurses run") is True


def test_is_palindrome_invalid():
    with pytest.raises(TypeError):
        is_palindrome(None)


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python") == "Python"


def test_capitalize_words_invalid():
    with pytest.raises(TypeError):
        capitalize_words(123)


def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("xyz") == 0
    assert count_vowels("AEIOU") == 4


def test_count_vowels_invalid():
    with pytest.raises(TypeError):
        count_vowels([])
