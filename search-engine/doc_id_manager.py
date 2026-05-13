from pathlib import Path
import json


class DocIdManager:
    def __init__(self, map_file="id_map/id_map.json"):
        self.map_file = Path(map_file)
        self.id_map = self.load()

    def load(self):
        if self.map_file.exists():
            with open(self.map_file, "r") as f:
                return json.load(f)
        return {}

    def save(self):
        self.map_file.parent.mkdir(parents=True, exist_ok=True)

        with open(self.map_file, "w") as f:
            json.dump(self.id_map, f, indent=4)

    def add_file(self, file_name):
        if file_name not in self.id_map:
            new_id = max(self.id_map.values(), default=-1) + 1
            self.id_map[file_name] = new_id
            self.save()

        return self.id_map[file_name]

    def build_map(self, documents_path="documents"):
        for file_path in Path(documents_path).glob("*.txt"):
            self.add_file(file_path.name)

    def get_id(self, file_name):
        return self.id_map[file_name]