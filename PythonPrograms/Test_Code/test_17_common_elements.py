import sys
from pathlib import Path
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
common_elements = importlib.import_module("Code.17_common_elements").common_elements

def test_common_elements():
    assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    assert common_elements([1, 2], [3, 4]) == []

if __name__ == "__main__":
    test_common_elements()
    print("All test cases passed.")