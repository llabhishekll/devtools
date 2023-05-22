# Devtools

![Python](https://img.shields.io/badge/python-3.10+-blue)

## Structure

``` text
.
├── pyproject.toml
├── requirements-dev.txt
├── requirements.txt
├── ... other config files ...
├── docs
│   ├── api.md
│   └── index.md
├── examples
│   └── main.py
├── package
│   ├── core
│   │   ├── __init__.py
│   │   ├── directory.py
│   │   ├── dotcleaner.py
│   │   └── rename.py
│   ├── __init__.py
│   ├── cli.py
│   └── version.py
└── tests
    ├── conftest.py
    └── test_package.py
```

## Commands

```sh
# install (local)
$ python -m venv venv
$ /venv/bin/pip install -e .
```

```sh
# ruff
$ ruff check .
$ ruff check --fix .
```

```sh
# pre-commit
$ pre-commit install
$ pre-commit run --all-files
```

```sh
# test
$ pytest .
```

```sh
# code coverage
$ pytest --cov=fastvector tests --cov-report=html
```

```sh
# mkdocs
$ mkdocs build
$ mkdocs serve
```

```sh
# build package
$ make
```

## Roadmap

- [X] dotcleaner
- [X] frename
    - [X] folder-rename
    - [ ] file-rename
- [ ] parser

See the [open issues](https://github.com/llabhishekll/devtools/issues) for a full list of proposed features (and known issues).

## Tools

Python tool/modules used for project development.

- `Lint` : [ruff](https://beta.ruff.rs/docs/rules/) inclusive of (`flake8` `pylint` `autopep8` `pydocstyle`), [mypy](https://www.mypy-lang.org/), [isort](https://pycqa.github.io/isort/) and [black](https://black.readthedocs.io/en/stable/).
- `Test` : [Pytest](https://docs.pytest.org/en/stable/) and [codecov](https://codecov.io).
- `Documentations` : [mkdocs](https://www.mkdocs.org/), [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) and [mkdocstrings](https://mkdocstrings.github.io/).
- `Build` : [build](https://pypa-build.readthedocs.io/en/latest/) and [twine](https://twine.readthedocs.io/en/stable/).
- `CI` : [pre-commit](https://github.com/pre-commit/pre-commit) and [github-actions](https://github.com/features/actions/).

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.
