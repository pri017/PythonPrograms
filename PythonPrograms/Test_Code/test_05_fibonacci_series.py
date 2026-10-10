import sys
from pathlib import Path
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
fibonacci = importlib.import_module("Code.05_fibonacci_series").fibonacci

def test_fibonacci():
    assert fibonacci(1) == [0]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(0) == []

if __name__ == "__main__":
    test_fibonacci()
    print("All test cases passed.")