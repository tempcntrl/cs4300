# Import functions from task3
from src.task3 import CheckNumber, First10Primes, Sum1To100


# Check if numbers return right positivity of themselves
def testCheckNumber():
    assert CheckNumber(5) == "positive"
    assert CheckNumber(-3) == "negative"
    assert CheckNumber(0) == "zero"

# Make sure the function returns the correct first 10 primes
def testFirst10Primes():
    assert First10Primes() == [2,3,5,7,11,13,17,19,23,29]

# Makes sure the sum of all numbers from 1 - 100 add correctly
def testSum1To100():
    assert Sum1To100() == 5050
