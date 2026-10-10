import sys
from pathlib import Path
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
is_prime = importlib.import_module("Code.06_prime_number").is_prime

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(4) is False
    assert is_prime(17) is True
    assert is_prime(1) is False

if __name__ == "__main__":
    test_is_prime()
    print("All test cases passed.")