import sys
from pathlib import Path
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
check_number = importlib.import_module("Code.03_pos_neg_zero").check_number

def test_check_number():
    assert check_number(10) == "Positive"
    assert check_number(-5) == "Negative"
    assert check_number(0) == "Zero"

if __name__ == "__main__":
    test_check_number()
    print("All test cases passed.")