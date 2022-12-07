import pytest
from interest_calculator.core import (
    simple_interest,
    compound_interest
)


@pytest.mark.skip(reason="Skipping this MODULE level test - Simple Interest")
def test_simple_interest_calculator() -> None:
    value = simple_interest(8, 6, 8)
    assert value == 3.84


# @pytest.mark.skip(reason="Skipping this MODULE level test - Compound Interest")
def test_compound_interest_calculator() -> None:
    # pytest.skip("Compound Interest Calculation Not Needed")
    value = compound_interest(10000, 2, 5)
    assert value == 110250000.0


@pytest.mark.skip(reason="Skipping this CLASS level test")
class TestInterestCalculator:
    def test_simple_interest_calculator(self) -> None:
        value = simple_interest(8, 6, 8)
        assert value == 3.84

    def test_compound_interest_calculator(self) -> None:
        value = compound_interest(10000, 2, 5)
        assert value == 110250000.0
