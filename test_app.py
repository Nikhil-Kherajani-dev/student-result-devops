from app import calculate_percentage, get_grade


def test_percentage():
    marks = [80, 90, 70]
    assert calculate_percentage(marks) == 80


def test_grade():
    assert get_grade(95) == "A+"
    assert get_grade(85) == "A"
    assert get_grade(75) == "B"
    assert get_grade(65) == "C"
    assert get_grade(55) == "D"
    assert get_grade(40) == "F"
