# Python Project Template
This is my personal template for Python projects and is work in progress (see [Next Steps](#next-steps)).

It is opinionated towards the usage of `pipenv` for dependency management, `black` for formatting and `flake8` for linting.

It includes the usage of `pre-commit` in order to be able to hook `black` and `flake8` in each commit to the repository, so that the code is not committed if it doesn't comply with the chosen standard formatting, very close --if not completely close-- to PEP8.

The idea is to enforce a code style and formatting that reduces the noise of the pull requests and is automated so that it doesn't introduce extra steps that I can forget about.

## Install Python 3 and `pipenv`
Install a stable release of Python 3 on your system, and then install `pipenv`. 

It is preferable to install `pipenv` in the user space in order to avoid breaking system-wide packages or Python installations. This applies especially to macOS and GNU/Linux, including Raspberry Pi OS, because they are known to have a lot of system components written in Python. To do that type `pip install --user pipenv` in the command line.

## Set Your Project Up
Let's make this project yours.
1. Clone this repository
2. Remove the `.git` directory with `rm -r project-template/.git`
3. Rename the directory to something that suits your project, e.g.: `mv project-template my-project`
4. Initialise your own git repository with `git init`

Now, let's initialise the Python virtual environment and all these helper tools.
1. Enter the directory and create a virtual environment by installing `pre-commit` with `pipenv install --dev pre-commit`
2. Change the line `language-version: python3.9` in `.pre-commit.config.yaml` so that matches the version under the line `[requires]` in the newly created `Pipfile`
3. Enter the Python virtual environment with `pipenv shell`
4.  Run `pre-commit install` to set up your hooks in your `.git/`
5.  Update the versions of `flake8` and `black` that are wrapped by `pre-commit` by running `pre-commit autoupdate`

## Try it Out
This project example includes a file, `hello.py`, with the following content:
```Python
print('Hello. The world is round, we\'ve been to the Moon, and the vaccines work.')
```
This file has some formatting problems according to `black` and the PEP8. 

After setting your project up, add the files and run an initial commit. You should see something like the following:

```zsh
(project-template) ➜  project-template git:(main) ✗ git commit -a -m "first commit"
black....................................................................Failed
- hook id: black
- files were modified by this hook

reformatted hello.py
All done! ✨ 🍰 ✨
1 file reformatted.

flake8...................................................................Passed
```
**The commit was aborted**, as the pre-commit tools didn't pass. However, `black` reformatted `hello.py`. If you now open it, you'll see that the code has changed to the following:
```Python
print(
    "Hello. The world is round, we've been to the Moon, and the vaccines work."
)

```
If now you repeat the commit, it will succeed. Finish setting it up with your real source code, write an appropriate `README.md`, check whether the `LICENSE` matches your interests, and set your remote Git repository.

# Next Steps
1. Check whether something can be automated re. the choice of a Unit Testing / BDD framework 
2. Add the configuration and metadata files for packaging

# References / Acknowledgements
My work mate Ajay for getting me in the right direction regarding `black` and `flake8`.

The `pre-commit` automation is taken from this [wonderful blog post by LJ Miranda](https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/).