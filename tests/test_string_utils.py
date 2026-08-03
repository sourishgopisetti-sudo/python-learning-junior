# test_string_utils.py
# Tests for string_utils.py

from string_utils import reverse_string, count_vowels, is_palindrome


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("abc") == "cba"


def test_count_vowels():
    assert count_vowels("hello world") == 3
    assert count_vowels("xyz") == 0


def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("race car") == True
    assert is_palindrome("hello") == False