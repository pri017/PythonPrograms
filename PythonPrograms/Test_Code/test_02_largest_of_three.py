import sys
from pathlib import Path
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
find_largest = importlib.import_module("Code.02_largest_of_three").find_largest

def test_find_largest():
    assert find_largest(10, 20, 30) == 30
    assert find_largest(50, 10, 30) == 50
    assert find_largest(5, 5, 5) == 5

if __name__ == "__main__":
    test_find_largest()
    print("All test cases passed.")