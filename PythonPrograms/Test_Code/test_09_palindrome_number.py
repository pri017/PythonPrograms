import sys
from pathlib import Path
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
is_palindrome_number = importlib.import_module("Code.09_palindrome_number").is_palindrome_number

def test_is_palindrome_number():
    assert is_palindrome_number(121) is True
    assert is_palindrome_number(-121) is False
    assert is_palindrome_number(123) is False

if __name__ == "__main__":
    test_is_palindrome_number()
    print("All test cases passed.")