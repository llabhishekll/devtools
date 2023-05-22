import pathlib
from typing import Any

import click

from devtools.core.dotcleaner import DirectoryMetaCleaner
from devtools.core.rename import DirectoryRename


CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.group(chain=True, context_settings=CONTEXT_SETTINGS)
def cli() -> None:
    pass


@cli.command("dotcleaner")
@click.option(
    "--path",
    "-p",
    default=".",
    help="Path to execute command.",
)
@click.option(
    "--file",
    "-f",
    default=".DS_Store",
    help="Remove dot file from the folder.",
)
def dot_cleaner(path: Any, file: Any) -> None:
    path = pathlib.Path(".") if path == "." else pathlib.Path(path)
    cleaner = DirectoryMetaCleaner(path=path)
    cleaner.dot_cleaner(remove_file=file)


@cli.command("frename")
@click.option(
    "--path",
    "-p",
    default=".",
    help="Path to execute command.",
)
def rename_directory(path: Any, file: Any) -> None:
    path = pathlib.Path(".") if path == "." else pathlib.Path(path)
    rename = DirectoryRename(path=path)
    rename.rename_directories(keywords=None)


if __name__ == "__main__":
    cli()
