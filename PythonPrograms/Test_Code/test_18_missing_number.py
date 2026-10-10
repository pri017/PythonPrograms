import sys
from pathlib import Path
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
find_missing_number = importlib.import_module("Code.18_missing_number").find_missing_number

def test_find_missing_number():
    assert find_missing_number([1, 2, 4, 5]) == 3
    assert find_missing_number([2, 3, 1, 5]) == 4

if __name__ == "__main__":
    test_find_missing_number()
    print("All test cases passed.")