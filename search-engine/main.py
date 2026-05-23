"""
Created by nzapi on 2026-05-14
"""
from boolean_query import BooleanQuery
from build_index import IndexManager


def main():
    index_manager = IndexManager()

    boolean_query = BooleanQuery()

    query = "(willing :and: die) :or: dust"
    tokenized_query = boolean_query.tokenize_boolean_query(query)

    print(boolean_query.answer(tokenized_query))


if __name__ == "__main__":
    main()
