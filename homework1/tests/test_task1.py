# Import hello worl file
from src.task1 import hello

# Function to check output is correct
def test_hello():
    assert hello() == "Hello, World!"
