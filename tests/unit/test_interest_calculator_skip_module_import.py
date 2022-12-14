import pytest
from interest_calculator.core import simple_interest, compound_interest

fake_library = pytest.importorskip("fake_library")


def test_simple_interest_calculator_module_import() -> None:
    value = simple_interest(8, 6, 8)
    assert value == 3.84


def test_compound_interest_calculator_module_import() -> None:
    value = compound_interest(10000, 2, 5)
    assert value == 110250000.0
