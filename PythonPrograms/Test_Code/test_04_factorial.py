import sys
from pathlib import Path
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
factorial = importlib.import_module("Code.04_factorial").factorial

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

if __name__ == "__main__":
    test_factorial()
    print("All test cases passed.")