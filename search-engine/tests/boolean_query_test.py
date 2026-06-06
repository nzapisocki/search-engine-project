from boolean_query import BooleanQuery


def test_boolean_and():
    docVec1 = ["0", "1", "2"]
    docVec2 = ["0", "2"]
    assert BooleanQuery.boolean_and(docVec1, docVec2) == ["0", "2"]

    docVec1 = ["0", "1", "2"]
    docVec2 = ["3", "4"]
    assert BooleanQuery.boolean_and(docVec1, docVec2) == []

    docVec1 = []
    docVec2 = ["3", "4"]
    assert BooleanQuery.boolean_and(docVec1, docVec2) == []

    docVec1 = []
    docVec2 = []
    assert BooleanQuery.boolean_and(docVec1, docVec2) == []


def test_boolean_or():
    docVec1 = ["0", "1", "2"]
    docVec2 = ["0", "2"]
    assert BooleanQuery.boolean_or(docVec1, docVec2) == ["0", "1", "2"]

    docVec1 = []
    docVec2 = ["3", "4"]
    assert BooleanQuery.boolean_or(docVec1, docVec2) == ["3", "4"]

    docVec1 = []
    docVec2 = []
    assert BooleanQuery.boolean_or(docVec1, docVec2) == []


if __name__ == "__main__":
    test_boolean_and()
