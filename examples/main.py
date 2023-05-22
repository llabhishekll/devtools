#!/usr/bin/env python3

from pathlib import Path

from devtools.core.directory import DirectoryManager


def main() -> None:
    path = Path(".")
    obj = DirectoryManager(path)
    obj.get_path_list()


if __name__ == "__main__":
    main()
