import pytest
from interest_calculator.core import (
    simple_interest,
    compound_interest
)

pytestmark = pytest.mark.skip("all tests still WIP")

def test_simple_interest_calculator_skip_all() -> None:
    value = simple_interest(8, 6, 8)
    assert value == 3.84


def test_compound_interest_calculator_skip_all() -> None:
    value = compound_interest(10000, 2, 5)
    assert value == 110250000.0
