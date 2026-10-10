import sys
from pathlib import Path
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
word_frequency = importlib.import_module("Code.20_word_frequency").word_frequency

def test_word_frequency():
    assert word_frequency("Hello world hello") == {"hello": 2, "world": 1}
    assert word_frequency("Test. Test, TEST!") == {"test": 3}

if __name__ == "__main__":
    test_word_frequency()
    print("All test cases passed.")