# Extends pythonic task management & command execution with file dependencies.

>

[![Latest Version on PyPI](https://img.shields.io/pypi/v/pyinvokedepends.svg)](https://pypi.python.org/pypi/pyinvokedepends/)
[![Supported Implementations](https://img.shields.io/pypi/pyversions/pyinvokedepends.svg)](https://pypi.python.org/pypi/pyinvokedepends/)

## Installation

The recommended way is to install the latest stable release via pip:
```
pip install pyinvokedepends
```

It's 2020, I only support Python 3.6+.

## Documentation

`pyinvokedepends` is an extension of [pyinvoke](https://www.pyinvoke.org/) to allow more "makefile" like task definitions.

It introduces an additional decorator `@depends` which can be used in addtion to [pyinvoke](https://www.pyinvoke.org/)'s decorator `@task`. Adding this decorator to a task will make sure that the task is only executed when any of `to` files is newer than one of the `created` files.

For a simple example, consider the following `tasks.py`. In contrast to traditional `make`, this will always run `gcc hello.c`

```
from invoke import task
@task
def compile(c):
  c.run("gcc hello.c", echo=True)
```

With `pyinvokedepends` we can add dependencies:

```
from invoke import task
from pyinvokedepends import depends
@depends(on=["./hello.c"], creates=["./a.out"])
@task
def test(c):
def compile(c):
  c.run("gcc hello.c", echo=True)
```

The task will only execute if the file `./hello.c` is newer than the file `./a.out`. Otherwise, the execution will be skipped.

The values of the parameters `on` and `creates` are lists of [`globs`](https://docs.python.org/3/library/glob.html). At lease one the files matching (one of) the `on` globs must exist. The task is executed
+ if no file exists which matches (any of) the `creates` globs, or
+ one of the files matching the `on` globs is newer than at least one file of the `creates` globs.

It does not automatically add `pre` or `post` steps to the task based on the dependencies.
