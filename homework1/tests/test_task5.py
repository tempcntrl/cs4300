from src.task5 import BooksDemo, StudentsDemo

def testBooksDemo():
    assert BooksDemo()[:3] == ["Book A", "Book B", "Book C"]

def testStudentsDemo():
    students = StudentsDemo()
    assert students["Alice"] == 1
    assert students["Bob"] == 2
