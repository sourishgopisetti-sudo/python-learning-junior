def reverse_string(s):
    """Return the reversed version of the input string."""
    return s[::-1]

def count_vowels(s):
    """Count the number of vowels in the input string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def is_palindrome(s):
    """Check if the input string is a palindrome (ignoring case and spaces)."""
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    print("Reverse of 'hello':", reverse_string("hello"))
    print("Vowels in 'hello world':", count_vowels("hello world"))
    print("Is 'racecar' a palindrome?", is_palindrome("racecar"))
    print("Is 'hello' a palindrome?", is_palindrome("hello"))