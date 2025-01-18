import pytest

def square(x:int):
    return x**2

def test_square():
    assert square(2) == 4, "test failed square of 2 is 4"
    assert square(4) == 16,"test failed square of 2 is 16"
    assert square(6) == 36,"test failed square of 2 is 36"

def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")