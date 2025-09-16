# Import book funcs from task5
from src.task5 import BooksDemo, StudentsDemo

# Test to make sure they return the correct list
def testBooksDemo():
    assert BooksDemo()[:3] == ["Book A", "Book B", "Book C"]

# Test to make sure theyare in the right pos
def testStudentsDemo():
    students = StudentsDemo()
    assert students["Alice"] == 1
    assert students["Bob"] == 2
