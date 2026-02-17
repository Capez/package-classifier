import pytest
from classifier import sort


def test_standard():
    assert sort(10, 10, 10, 5) == "STANDARD"


def test_bulky_is_special():
    assert sort(100, 100, 100, 10) == "SPECIAL"


def test_heavy_is_special():
    assert sort(10, 10, 10, 20) == "SPECIAL"


def test_bulky_and_heavy_is_rejected():
    assert sort(100, 100, 100, 20) == "REJECTED"


def test_just_under_limits_is_standard():
    assert sort(99, 99, 99, 19) == "STANDARD"


def test_at_volume_limit_under_mass_is_special():
    assert sort(100, 100, 100, 19) == "SPECIAL"


def test_zero_mass_is_standard():
    assert sort(10, 10, 10, 0) == "STANDARD"


def test_negative_input_raises():
    with pytest.raises(ValueError):
        sort(-1, 10, 10, 5)
    with pytest.raises(ValueError):
        sort(10, 10, 10, -1)
