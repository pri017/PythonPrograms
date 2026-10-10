import sys
from pathlib import Path
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
reverse_number = importlib.import_module("Code.08_reverse_number").reverse_number

def test_reverse_number():
    assert reverse_number(1234) == 4321
    assert reverse_number(-560) == -65
    assert reverse_number(7) == 7

if __name__ == "__main__":
    test_reverse_number()
    print("All test cases passed.")