from pathlib import Path

from devtools.core.directory import DirectoryManager


__all__ = ["DirectoryMetaCleaner"]


class DirectoryMetaCleaner(DirectoryManager):
    """A class to find `.` dot files and remove them.

    Args:
        DirectoryManager (object): Path finding
    """

    def __init__(self, path: Path | None) -> None:
        super().__init__(path)

    def dot_finder(self) -> list:
        files = []
        for path in self.get_files():
            if path.name.startswith("."):
                files.append(path)
        return files

    def dot_cleaner(self, remove_file: str) -> None:
        for path in self.dot_finder():
            if path.name == remove_file:
                path.unlink()
                print(f"removing {path}")


if __name__ == "__main__":
    pass
