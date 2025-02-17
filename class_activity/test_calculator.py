import pytest
from main import add, subtract, multiply, factorial, is_prime, power

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0.5, 0.5) == 1.0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(1, -1) == 2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(-2, -2) == 4

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(1) == False

def test_power():
    assert power(2, 3) == 8
    assert power(3, 0) == 1
    assert power(0, 5) == 0

