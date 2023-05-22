#!/usr/bin/env python3
from pathlib import Path

from devtools.core.directory import DirectoryManager


class DirectoryRename(DirectoryManager):
    """A class to find folder and rename them.

    Args:
        DirectoryManager (object): Path finding
    """

    def __init__(self, path: Path) -> None:
        super().__init__(path)

    def rename_file(self, file_name: str, new_name: str) -> list:
        new_paths = []
        for path in self.find_file(file_name=file_name):
            new_path = path.with_name(new_name)
            path.replace(new_path)
            new_paths.append(new_path)
        return new_paths

    def rename_directories(self, keywords: dict | None) -> None:
        keywords = {"_": "-", " ": "-"} if keywords is None else keywords
        new_paths = []
        for path in self.get_directories():
            new_name = path.name.lower()
            for keyword, value in keywords.items():
                new_name = new_name.replace(keyword, value)
            new_path = path.with_name(new_name)
            path.replace(new_path)
            new_paths.append(new_path)
            print(f"renamed {new_paths}")


if __name__ == "__main__":
    pass
