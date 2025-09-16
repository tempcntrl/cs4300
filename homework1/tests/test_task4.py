from src.task4 import CalculateDiscount

def testCalculateDiscount():
    assert CalculateDiscount(100, 20) == 80
    assert CalculateDiscount(50.0, 10.0) == 45.0
