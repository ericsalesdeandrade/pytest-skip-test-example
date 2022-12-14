import sys
import pytest
from interest_calculator.core import simple_interest, compound_interest


@pytest.mark.skip(reason="Skipping this FUNCTION level test - Simple Interest")
def test_simple_interest_calculator_function() -> None:
    value = simple_interest(8, 6, 8)
    assert value == 3.84


def test_compound_interest_calculator_function() -> None:
    # pytest.skip("Compound Interest Calculation Not Needed")
    value = compound_interest(10000, 2, 5)
    assert value == 110250000.0


@pytest.mark.skip(reason="Skipping this CLASS level test")
class TestInterestCalculator:
    def test_simple_interest_calculator_class(self) -> None:
        value = simple_interest(8, 6, 8)
        assert value == 3.84

    def test_compound_interest_calculator_class(self) -> None:
        value = compound_interest(10000, 2, 5)
        assert value == 110250000.0


@pytest.mark.skipif(
    sys.version_info >= (3, 10), reason="requires lower than python3.10"
)
def test_simple_interest_calculator_py_version() -> None:
    value = simple_interest(8, 6, 8)
    assert value == 3.84


@pytest.mark.skipif(sys.version_info >= (3, 10),
                    reason="requires lower than python3.10")
def test_compound_interest_calculator_py_version() -> None:
    value = compound_interest(10000, 2, 5)
    assert value == 110250000.0
