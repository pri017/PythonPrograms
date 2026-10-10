import sys
from pathlib import Path
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
is_palindrome_string = importlib.import_module("Code.13_palindrome_string").is_palindrome_string

def test_is_palindrome_string():
    assert is_palindrome_string("madam") is True
    assert is_palindrome_string("Racecar") is True
    assert is_palindrome_string("hello") is False

if __name__ == "__main__":
    test_is_palindrome_string()
    print("All test cases passed.")