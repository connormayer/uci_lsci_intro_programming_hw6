from shapes import Rectangle, Circle, RightTriangle, Square
from nltk_word_counts import get_most_frequent_words

def test_rectangle():
    rect = Rectangle(10, 5)
    assert rect.get_perimeter() == 30
    assert rect.get_area() == 50

def test_circle():
    circ = Circle(3)
    assert circ.get_perimeter() == 18.84955592153876
    assert circ.get_area() == 28.274333882308138

def test_right_triangle():
    tri = RightTriangle(3, 4)
    assert tri.get_perimeter() == 12
    assert tri.get_area() == 6

def test_square():
    square = Square(5)
    assert square.get_perimeter() == 20
    assert square.get_area() == 25

    # Check that get_perimeter and get_area have not been ovewritten
    assert "get_area" not in Square.__dict__
    assert "get_perimeter" not in Square.__dict__

def test_frequent_words():
    result = get_most_frequent_words('data/austen-sense.txt')
    assert result == [
        ('I', 2003), ("'s", 700), ('Elinor', 683), ('could', 568), ('Marianne', 565), 
        ('Mrs.', 523), ('would', 507), ('said', 396), ('every', 361), ('one', 303)
    ]

    result = get_most_frequent_words('data/austen-sense.txt', 5)
    assert result == [
        ('I', 2003), ("'s", 700), ('Elinor', 683), ('could', 568), ('Marianne', 565)
    ]

