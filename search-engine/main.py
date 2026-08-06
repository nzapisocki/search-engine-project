"""
Created by nzapi on 2026-05-14
"""
from boolean_query import BooleanQuery
from doc_id_manager import DocIdManager
from index_manager import IndexManager


def main():
    index_manager = IndexManager()
    boolean_query = BooleanQuery(DocIdManager(), IndexManager())

    query = "johnny depp amber heard"
    tokenized_query = boolean_query.tokenize_boolean_query(query)

    print(tokenized_query)
    # print(boolean_query.answer(tokenized_query))


if __name__ == "__main__":
    main()
