import sys
from pathlib import Path
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
remove_duplicates = importlib.import_module("Code.16_remove_duplicates").remove_duplicates

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 1]) == [1, 2, 3, 4]
    assert remove_duplicates([]) == []

if __name__ == "__main__":
    test_remove_duplicates()
    print("All test cases passed.")