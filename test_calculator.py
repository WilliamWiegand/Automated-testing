import pytest
from calculator import add, divide 

def test_add_pass():
    result = add(4, 10)
    assert result == 14

def test_add_fail():
    result = add(4, 10) 
    assert result == 15 
