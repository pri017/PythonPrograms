import importlib
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Import module starting with digits dynamically
even_odd_module = importlib.import_module("Code.01_even_odd")
check_even_odd = even_odd_module.check_even_odd


def test_check_even_odd():
  assert check_even_odd(4) == "Even"
  assert check_even_odd(7) == "Odd"
  assert check_even_odd(0) == "Even"
  assert check_even_odd(-2) == "Even"
  assert check_even_odd(-3) == "Odd"


if __name__ == "__main__":
  test_check_even_odd()
  print("All test cases passed.")