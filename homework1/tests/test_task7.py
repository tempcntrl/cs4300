from src.task7 import GetStatus

def testGetStatus():
    assert GetStatus("https://httpbin.org/status/200") == 200
