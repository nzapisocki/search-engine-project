"""
Created by nzapi on 2026-05-14
"""

from build_index import IndexManager


def main():
    index_manager = IndexManager()
    print(index_manager.get_index())


if __name__ == "__main__":
    main()
