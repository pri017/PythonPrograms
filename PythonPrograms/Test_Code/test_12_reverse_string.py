import sys
from pathlib import Path
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
reverse_string = importlib.import_module("Code.12_reverse_string").reverse_string

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("abcba") == "abcba"

if __name__ == "__main__":
    test_reverse_string()
    print("All test cases passed.")