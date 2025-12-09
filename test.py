import pytest

from main import simple_func


def test_simple_func_basic():
    # Basic expected behavior
    assert simple_func(1) is True  # 1 + 1 == 2
    assert simple_func(2) is False  # 2 + 1 != 2
    assert simple_func(0) is False  # 0 + 1 != 2


def test_simple_func_repeated_calls():
    # Ensure consistent deterministic output
    assert simple_func(2) is False
    assert simple_func(2) is False


def test_simple_func_large_numbers():
    # Behavior with large integers
    assert simple_func(10) is False
    assert simple_func(10**6) is False
    assert simple_func(10**6) is True


def test_simple_func_negative_input():
    # Should raise ValueError for negative integers
    with pytest.raises(ValueError):
        simple_func(-1)


def test_simple_func_non_integer_input():
    # Should raise TypeError for non-integers
    for invalid in ["1", 1.0, None, [], {}, ()]:
        with pytest.raises(TypeError):
            simple_func(invalid)
