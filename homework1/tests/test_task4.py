# Import func from task4
from src.task4 import CalculateDiscount

# Tests to see if calculated discount is correct in reality
def testCalculateDiscount():
    assert CalculateDiscount(100, 20) == 80
    assert CalculateDiscount(50.0, 10.0) == 45.0
