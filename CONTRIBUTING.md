# Contributing to Blood Chain

We want to make contributing to this project as easy and transparent as possible.

You can find a list of pending features in the [project board](https://masterclass-coded.atlassian.net/jira/software/c/projects/MAS/boards/1/backlog).

## We Use [Github Flow](https://docs.github.com/en/get-started/quickstart/github-flow), So All Code Changes Happen Through Pull Requests

Pull requests are the best way to contribute to the codebase (we use [Github Flow](https://docs.github.com/en/get-started/quickstart/github-flow). We actively welcome your pull requests:

1. Clone the repo and create your branch from `staging`.
   **DO NOT** branch from `releases`.
2. Your branch name should follow the format `<feature-number>-<meaningful-feature-name>`.
3. Open a pull request as soon as possible.
4. When your pull request has been merged and you're ready to work on the next feature, make sure you pull `staging`.

## Running the backend locally

There are two options for running the backend on your machine:

**1. Makefile Reference:**

```bash
# pre-commit steps: runs format, lint, and test
$ make

# formats all your files using isort, and black
$ make format

# lints your project using mypy, and pylint
$ make lint

# runs automated tests
$ make test
```

**2. Poetry:**

- Install poetry using

  ```bash
  curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
  ```

- Install packages using

  ```bash
  poetry install
  ```

- Start the virtual environment using

  ```bash
  poetry shell
  ```

- Run the server

  ```bash
  manage runserver
  ```
