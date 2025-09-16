# Imports function from task 6
from src.task6 import CountWords

# Test to see if text from the readmy counts correctly
def testCountWords():
    assert CountWords("src/task6_read_me.txt") == 104
