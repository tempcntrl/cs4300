# Import func from task 7
from src.task7 import GetStatus

# Test to see if web info returns correct status
def testGetStatus():
    assert GetStatus("https://httpbin.org/status/200") == 200
