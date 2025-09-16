# Import values from task2
from src.task2 import my_int, my_float, my_string, my_bool

# Tests if they are correct
def test_variables():
    assert isinstance(my_int, int)
    assert isinstance(my_float, float)
    assert isinstance(my_string, str)
    assert isinstance(my_bool, bool)

