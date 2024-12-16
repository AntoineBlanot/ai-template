poetry config virtualenvs.in-project true
poetry install --with dev
poetry run pre-commit install
