from src.task3 import CheckNumber, First10Primes, Sum1To100

def testCheckNumber():
    assert CheckNumber(5) == "positive"
    assert CheckNumber(-3) == "negative"
    assert CheckNumber(0) == "zero"

def testFirst10Primes():
    assert First10Primes() == [2,3,5,7,11,13,17,19,23,29]

def testSum1To100():
    assert Sum1To100() == 5050
