from pathlib import Path


__all__ = ["DirectoryManager"]


class DirectoryManager:
    """A class to manage path finding and bifercation.
    """
    def __init__(self, path: Path | None) -> None:
        if path is None:
            self.path = Path(".")
        elif isinstance(path, Path):
            self.path = path
        else:
            raise ValueError("Object of type `pathlib.path` required.")

    def __str__(self) -> str:
        return self.path.name

    def get_path_list(self) -> list:
        paths = []
        for path in self.path.glob("**/*"):
            paths.append(path)
        return paths

    def get_directories(self) -> list:
        directory = []
        for path in self.get_path_list():
            if path.is_dir():
                directory.append(path)
        return directory

    def get_files(self) -> list:
        files = []
        for path in self.get_path_list():
            if path.is_file():
                files.append(path)
        return files

    def find_extension(self, ext: str) -> list:
        files = []
        for path in self.get_files():
            if path.suffix == ext:
                files.append(path)
        return files

    def find_file(self, file_name: str) -> list:
        files = []
        for path in self.get_files():
            if path.parts[-1].lower() == file_name:
                files.append(path)
        return files


if __name__ == "__main__":
    pass
