# Project
Description of the project.

## Installation
This project uses [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) for dependency management and packaging. While you are not required to use Poetry to install or run this project, it is a requirement for development, especially if you want to add new or upgrade existing dependencies.

This project also depends on Python version **3.10** so make sure you have a Python available with the corresponding version.

First, install Poetry as follow:
```bash
curl -sSL https://install.python-poetry.org | <your-python-path> -
```

Then, you can install the project as follow:
```bash
bash scripts/install.sh
# for dev: bash scripts/install-dev.sh
```

## Run
You can run any command in the project as follow:
```bash
poetry run <your-command>
```
