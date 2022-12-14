import sys
import pytest
from interest_calculator.core import simple_interest, compound_interest


@pytest.mark.xfail(reason="Missing Arguments")
def test_simple_interest_calculator_xfail_missing_arg() -> None:
    value = simple_interest(8)  # Missing Argument - FAIL
    assert value == 3.84


@pytest.mark.xfail(reason="Missing Arguments")
def test_compound_interest_calculator_xfail_missing_arg() -> None:
    value = compound_interest(2, 5)  # Missing Argument - FAIL
    assert value == 110250000.0


@pytest.mark.xfail(raises=TypeError)
def test_simple_interest_calculator_xfail_raise_error() -> None:
    value = simple_interest(8)  # Missing Argument - FAIL - Raise Type Error
    assert value == 3.84
