# this file will create a map of file names to docIDs

from pathlib import Path
from collections import defaultdict
import json

''' Add a new file to the id map
    Args:
        id_map: the map
        file_name: name of the file to map'''


def add_file(id_map, file_name):
    if file_name not in id_map:
        doc_id = max(id_map.values(), default=-1) + 1
        id_map[file_name] = doc_id


if __name__ == '__main__':
    data_path = Path("documents")

    doc_id_map = defaultdict(dict)

    for file_path in data_path.glob("*txt"):
        add_file(doc_id_map, file_path.name)

    with open("id_map/id_map.json", "w") as f:
        json.dump(doc_id_map, f, indent=4)
