import sys
from pathlib import Path
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
count_vowels_consonants = importlib.import_module("Code.11_vowels_consonants").count_vowels_consonants

def test_count_vowels_consonants():
    assert count_vowels_consonants("hello") == (2, 3)
    assert count_vowels_consonants("Python 123") == (1, 5)

if __name__ == "__main__":
    test_count_vowels_consonants()
    print("All test cases passed.")