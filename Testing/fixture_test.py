import pytest
from typing import List


class Fruit:
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture
def my_fruit():
    return Fruit("apple")

@pytest.fixture
def exotic_fruit():
    return Fruit("mango")

@pytest.fixture
def fruit_basket(my_fruit, exotic_fruit):
    return [Fruit("banana"), my_fruit, exotic_fruit]

def test_my_fruit_in_basket(my_fruit: Fruit, fruit_basket: List):
    assert my_fruit in fruit_basket
    
@pytest.mark.parametrize("fruit_name,expected_result", [
    ("apple", True),
    ("banana", True),
    ("orange", False),
    ("mango", True)])
def test_eval(fruit_name: str, expected_result: bool, fruit_basket: List):
    assert (Fruit(fruit_name) in fruit_basket) == expected_result
    