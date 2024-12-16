> [!NOTE]
> Change every `package_name` instance of the template before usage.

# package_name
package_name description.

## Installation
This project uses [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) for dependency management and packaging.

This project also depends on Python version **3.10** so make sure you have a Python available with the corresponding version.

First, install Poetry as follow:
```bash
curl -sSL https://install.python-poetry.org | python3.10 -
```

Then, you can install the project as follow:
```bash
bash scripts/install.sh
```

## Run
You can run any command in the project as follow:
```bash
poetry run <your-command>
```
