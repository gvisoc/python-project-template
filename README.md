# Python Project Template
This is my personal template for Python projects and is a work in progress (see [Next Steps](#next-steps)).

I tested it using Pipenv for dependency management, and includes configuration files to use Black as the formatter and Flake8 as the style checker. They can be hooked to the Git workflow by means of the pre-commit Python package.

- `.pre-commit-config.yaml` configures `pre-commit` and downloads the proper versions of Black and Flake8 as needed
- `.flake8`: configuration file for itself
- `pyproject.toml` configures Black

The chosen standard formatting is very close to [PEP 8](https://www.python.org/dev/peps/pep-0008/), if not "PEP 8 strict".


The idea is to enforce a code style and formatting that reduces false differences the pull requests, due to formatting differences. It is also good for it to be automated, so that it doesn't introduce extra steps that can be forgotten.

## Install Python 3 and Pipenv
Install a stable release of Python 3 on your system, and then install Pipenv. 

It is preferable to install Pipenv in the user space in order to avoid breaking system-wide packages or Python installations. This applies especially to macOS and GNU/Linux, including Raspberry Pi OS, because they are known to have a lot of system components written in Python. To do that, type `pip install --user pipenv` in the command line, and then add the relevant directories to the `$PATH` variable.

## Set Your Project Up
Let's make this project yours.
1. Clone this repository
2. Remove the `.git` directory with `rm -r project-template/.git`
3. Rename the directory to something that suits your project, e.g.: `mv project-template my-project`
4. Initialise your own git repository with `git init`

Now, let's initialise the Python virtual environment and all these helper tools.
1. Enter the directory and create a virtual environment by installing pre-commit: `pipenv install --dev pre-commit`
2. Change the line `language-version: python3.9` in `.pre-commit-config.yaml` so that it matches the version under the line `[requires]` of the newly created `Pipfile`
3. Enter the Python virtual environment with `pipenv shell`
4.  Run `pre-commit install` to set up your hooks in your `.git/`
5.  Update the versions of `flake8` and `black` that are wrapped by pre-commit, by running `pre-commit autoupdate`

## Try it Out
This project example includes a file, `hello.py`, with the following content:

```Python
print('Hello. The world is round, we\'ve been to the Moon, and the vaccines work.')
```

This file has some formatting problems according to Black, Flake8, and the PEP 8. 

After setting your project up, add the files and run an initial commit. You should see something like the following:

```zsh
(my-project) ➜  my-project git:(main) ✗ git commit -a -m "Initial Commit"
black....................................................................Failed
- hook id: black
- files were modified by this hook

reformatted hello.py
All done! ✨ 🍰 ✨
1 file reformatted.

flake8...................................................................Passed
```

**The commit was aborted**, as Black failed. However, it reformatted `hello.py` and that made Flake8 to pass. If you now open it, you'll see that the code has changed to the following:

```Python
print(
    "Hello. The world is round, we've been to the Moon, and the vaccines work."
)
```

If now you repeat the commit, it will succeed because Black will find nothing to do, and Flake8 will still obviously pass. 

Finish setting it up with your real source code, write an appropriate `README.md`, check whether the `LICENSE` matches your interests, and set your remote Git repository.

# Next Steps
- See if something can be automated regarding the choice of a Unit Testing / BDD framework 
- Add configuration and metadata resources for packaging

# References / Acknowledgements
Thanks to: 
- My work mate Ajay for getting me in the right direction regarding Back and Flake8.
- The pre-commit automation is taken from this [wonderful blog post by LJ Miranda](https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/).

## Further Reading
- Pipenv: Python Dev Workflow for Humans ([website](https://pipenv.pypa.io/en/latest/))
- Black, the Uncompromising Code Formatter ([at GitHub](https://github.com/psf/black))
- Flake8, Your Tool for Style Guide Enforcement ([website](https://flake8.pycqa.org/en/latest/))
- Style Guide for Python Code, defined in [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- `pyproject.toml` is defined in [PEP 518](https://www.python.org/dev/peps/pep-0518/)
