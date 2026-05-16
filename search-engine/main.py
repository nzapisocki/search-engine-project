"""
Created by nzapi on 2026-05-14
"""
from boolean_query import BooleanQuery
from build_index import IndexManager


def main():
    index_manager = IndexManager()
    # print(index_manager.get_index())
    boolean_query = BooleanQuery()
    print(boolean_query.boolean_and("willing", "want", index_manager.get_index()))


if __name__ == "__main__":
    main()
