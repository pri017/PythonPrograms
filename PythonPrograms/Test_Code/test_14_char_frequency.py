import sys
from pathlib import Path
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
char_frequency = importlib.import_module("Code.14_char_frequency").char_frequency

def test_char_frequency():
    assert char_frequency("apple") == {"a": 1, "p": 2, "l": 1, "e": 1}
    assert char_frequency("") == {}

if __name__ == "__main__":
    test_char_frequency()
    print("All test cases passed.")