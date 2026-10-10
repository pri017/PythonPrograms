import sys
from pathlib import Path
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
find_duplicates = importlib.import_module("Code.19_find_duplicates").find_duplicates

def test_find_duplicates():
    assert find_duplicates([1, 2, 3, 2, 4, 5, 1]) == [1, 2]
    assert find_duplicates([1, 2, 3]) == []

if __name__ == "__main__":
    test_find_duplicates()
    print("All test cases passed.")