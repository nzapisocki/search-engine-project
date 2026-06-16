from boolean_query import BooleanQuery
from fake_doc_id_manager import FakeDocIdManager
from fake_index_manager import FakeIndexManager

fdim = FakeDocIdManager()
fim = FakeIndexManager()

boolQuery = BooleanQuery(fdim, fim)


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


def test_boolean_not():
    term_vector = ['0', '1']
    assert boolQuery.boolean_not(term_vector) == ['2']


def test_tokenize_query():
    query = "(testing    :and: fallout)  "
    tokenized_query = ["(", "testing", ":and:", "fallout", ")"]
    assert BooleanQuery.tokenize_boolean_query(query) == tokenized_query


def test_solve_expression():
    stack = ["(", ['0', '1'], ":and:", ['0']]
    assert boolQuery.solveExpression(stack) == ['0']

    stack = ["(", ":not:", "dummy"]
    assert boolQuery.solveExpression(stack) == ['0', '1', '2']

    stack = ["(", ['0', '1'], ":or:", ['2', '3']]
    assert boolQuery.solveExpression(stack) == ['0', '1', '2', '3']


def test_answer():
    tokenized_expression = ["(", "dum", ":and:", "test", ")"]
    assert boolQuery.answer(tokenized_expression) == []

    tokenized_expression = ["(", "dum", ":or:", "test", ")"]
    assert boolQuery.answer(tokenized_expression) == ["32", "69"]

    tokenized_expression = ["(", "dum", ")"]
    assert boolQuery.answer(tokenized_expression) == ["69"]

    tokenized_expression = ["(", ":not:", "dum", ")"]
    assert boolQuery.answer(tokenized_expression) == fdim.get_all_id()

    tokenized_expression = ["(", "test", ":or:", "dum", ":or:", "fall", ")"]
    assert boolQuery.answer(tokenized_expression) == ["32", "69"]


if __name__ == "__main__":
    test_boolean_and()
    test_boolean_or()
    test_tokenize_query()
    test_boolean_not()
    test_solve_expression()
    test_answer()
