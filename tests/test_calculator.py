"""Unit tests for the calculator module."""

import pytest

from src.calculator import add, divide, multiply, power, subtract


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -4) == -5

    def test_mixed_sign(self):
        assert add(-3, 7) == 4

    def test_floats(self):
        assert add(1.5, 2.5) == 4.0

    def test_zero(self):
        assert add(0, 0) == 0


class TestSubtract:
    def test_positive_result(self):
        assert subtract(10, 4) == 6

    def test_negative_result(self):
        assert subtract(3, 8) == -5

    def test_zero_result(self):
        assert subtract(5, 5) == 0


class TestMultiply:
    def test_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(5, 0) == 0

    def test_negative_numbers(self):
        assert multiply(-2, -3) == 6

    def test_mixed_sign(self):
        assert multiply(-2, 3) == -6


class TestDivide:
    def test_exact_division(self):
        assert divide(10, 2) == 5.0

    def test_float_result(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_negative_divisor(self):
        assert divide(-6, 2) == -3.0


class TestPower:
    def test_positive_exponent(self):
        assert power(2, 10) == 1024

    def test_zero_exponent(self):
        assert power(99, 0) == 1

    def test_negative_exponent(self):
        assert power(2, -1) == 0.5

    def test_base_zero(self):
        assert power(0, 5) == 0
