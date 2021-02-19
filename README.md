# Python Project Template
This is my personal template for Python **module** projects, and it is a work in progress (see [Next Steps](#next-steps)).

It is based on Poetry, and includes configuration sections in `pyproject.toml` to use Black as the formatter and Flake8 as the style checker. They can be hooked to the Git workflow by means of the pre-commit Python package. It also uses Pytest with Pytest-cov to run unit tests and test coverage reports.

- `.pre-commit-config.yaml` configures `pre-commit` and downloads the proper versions of Black and Flake8 as needed
- `pyproject.toml` holds the rest of the configuration.

The chosen standard formatting is very close to [PEP 8](https://www.python.org/dev/peps/pep-0008/), if not "PEP 8 strict".

The idea is to enforce a code style and formatting that reduces false differences the pull requests, due to formatting differences. It is also good for it to be automated, so that it doesn't introduce extra steps that can be forgotten.

## Install Python 3 and Poetry
Install a stable release of [Python 3](https://python.org) on your system, and then install Poetry. Poetry provides an installation script with support for maintenance operations; check [its own instructions](https://python-poetry.org/docs/#installation).


## Clone and Play With This Repository
Clone this repository to start.

Initialise the Python virtual environment and all these helper tools.
1. Install all the dependencies preconfigured in this repo by executing `poetry install`
2. Check that the line `language-version: python3.9` in `.pre-commit-config.yaml` still matches the version under the line `[tool.poetry.dependencies]` of the file `pyproject.toml`; this might have been updated by the previous command. If needed, update the line accordingly.
3.  Run `poetry run pre-commit install` to set up your hooks in your `.git/`
4.  Update the versions of Flake8 and Black that are wrapped by pre-commit, by running `poetry run pre-commit autoupdate`

## Try it Out
Have a look to the Python code inside the `example` module, `example/hello.py`, which includes a function called `inc`:

```Python
def inc(i):
    """Increments the operand."""
    return i + 1
```

### Try The Git Workflow Enhanced with a Code Formatter and a Style Checker 
The first thing that can be tried is to break the formatting of the file. Add some spaces around the `i` parameter:

```Python
def inc( i ):
    """Increments the operand."""
    return i + 1
```

Now, try to commit the code with `git add . && git commit -a -m "test commit"`.

You should see someting similar to the following:

```zsh
black....................................................................Failed
- hook id: black
- files were modified by this hook

reformatted hello.py
All done! ✨ 🍰 ✨
1 file reformatted.

flake8...................................................................Passed
```

**The commit was abandoned**, as Black failed. However, it reformatted `hello.py` and that made Flake8 to pass. If you now open it, you'll see that the code has changed back to the original content:

```Python
def inc(i):
    """Increments the operand."""
    return i + 1
```

If now you repeat the commit, it will succeed because Black will find nothing to do, and Flake8 will still obviously pass. 

### Try the Testing Framework
Execute the tests with the following sentence: `poetry run pytest --cov=example -n 2 --cov-fail-under=85`. The parameters mean the following:

- `--cov=example` narrows the coverage report to the module inside the project, to ignore other libraries and the tests themselves.
- `-n 2` uses a multiprocess factor of 2 to run the tests, using the pytest-xdist plugin
- `--cov-fail-under=85` allows us to fail the testing process (invalidate) if the coverage level is under 85%

You will see the following:

```zsh
================================== test session starts ===================================
platform linux -- Python 3.9.1, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: /home/gabriel/ws/python/python-project-template
plugins: xdist-2.2.1, cov-2.11.1, forked-1.3.0
gw0 [1] / gw1 [1]
.                                                                                  [100%]

----------- coverage: platform linux, python 3.9.1-final-0 -----------
Name                  Stmts   Miss  Cover
-----------------------------------------
example/__init__.py       1      0   100%
example/hello.py          2      0   100%
-----------------------------------------
TOTAL                     3      0   100%

Required test coverage of 85% reached. Total coverage: 100.00%
=================================== 1 passed in 0.30s ====================================
```
This returns to the system the exit code 0:
```zsh
$ echo $?
0
```

Try now to modify the file `tests/test_hello.py` from this:
```Python
import pytest
from example.hello import inc


def test_inc():
    assert inc(5) == 6
```
to this:
```Python
import pytest
from example.hello import inc


def test_inc():
    assert True
```
This test won't use our module at all, so the coverage level will fall. Repeat the same test execution sentence. Now you'll see an error report due to the coverage level failing below 85%:
```zsh
$ poetry run pytest --cov=example -n 2 --cov-fail-under=85  
================================== test session starts ===================================
platform linux -- Python 3.9.1, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: /home/gabriel/ws/python/python-project-template
plugins: xdist-2.2.1, cov-2.11.1, forked-1.3.0
gw0 [1] / gw1 [1]
.                                                                                  [100%]

----------- coverage: platform linux, python 3.9.1-final-0 -----------
Name                  Stmts   Miss  Cover
-----------------------------------------
example/__init__.py       1      0   100%
example/hello.py          2      1    50%
-----------------------------------------
TOTAL                     3      1    67%

FAIL Required test coverage of 85% not reached. Total coverage: 66.67%
=================================== 1 passed in 0.30s ====================================
```
Now the last 2 lines can be confusing, because we see "FAIL" and also "1 passed". This means that, although the test passed (`assert True` is always a pass), the overall process failed and this execution will return the Unix exit code 1. This will allow us to stop continuous build, continous integration or deployment pipelines:
```zsh
$ echo $?
1
```

### Packaging the Module
Poetry makes the packaging of the module as easy as running `poetry build`. Check [its documentation](https://python-poetry.org/docs/) for more information.

## Reproduce for Your Project
The way to use this template is no longer to copy and tweak this project. Instead, you can reproduce most of it yourself. Begin by using the following sequence of commands:

```zsh
$ poetry new my-project
$ cd my-project
$ git init .
# this will start an interactive process; fill the data
$ poetry add --dev pytest pytest-cov pytest-xdist pre-commit flake8 black
```
The above will initialise the project for both Git and Poetry, with a predefined structure for a module and also with support for unit tests. Do not forget to set a `.gitignore` file that works for your environment.

Now create a file named `.pre-commit-config.yaml` at the project root, and set it up with the hooks for Black and Flake8:
```yaml
repos:
-   repo: https://github.com/ambv/black
    rev: "20.8b1"
    hooks:
    - id: black
      language_version: python3.9
-   repo: https://gitlab.com/pycqa/flake8
    rev: "3.8.4"
    hooks:
    - id: flake8
```

Open the file `pyproject.toml` that has been created by Poetry and add the following configuration, or some other you'd prefer, for Black and Flake8:
```toml
[tool.flake8]
ignore = "E203, E266, E501, W503, F403, F401"
max-line-length = 79
max-complexity = 18
select = "B,C,E,F,W,T4,B9"

[tool.black]
line-length = 79
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''
```
Finish wiring these two tools with the pre-commit stage of Git:
```zsh
$ poetry run pre-commit install
$ poetry run pre-commit auto-update
```

All done; time to do some Python-fu.

# Next Steps
- Test a CI integration with Poetry.

# References / Acknowledgements
Thanks to: 
- My work mate Ajay for getting me in the right direction regarding Back and Flake8.
- The pre-commit automation is taken from this [wonderful blog post by LJ Miranda](https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/).

## Further Reading
- Poetry, Python packaging and dependency management made easy ([website](https://python-poetry.org/))
- Pytest, helps you write better programs ([documentation at its website](https://docs.pytest.org/en/stable/index.html))
- Black, the Uncompromising Code Formatter ([at GitHub](https://github.com/psf/black))
- Flake8, Your Tool for Style Guide Enforcement ([website](https://flake8.pycqa.org/en/latest/))
- Style Guide for Python Code, defined in [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- `pyproject.toml` is defined in [PEP 518](https://www.python.org/dev/peps/pep-0518/)