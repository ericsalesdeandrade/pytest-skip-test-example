import sys
import pytest
from interest_calculator.core import simple_interest, compound_interest

pytestmark = pytest.mark.skipif(
    sys.platform == "darwin", reason="tests for Windows only"
)


def test_simple_interest_calculator_platform() -> None:
    value = simple_interest(8, 6, 8)
    assert value == 3.84


def test_compound_interest_calculator__platform() -> None:
    value = compound_interest(10000, 2, 5)
    assert value == 110250000.0
