# python-postgresql-backend
This repo is started by following instruction on this [link](https://stackabuse.com/working-with-postgresql-in-python/). This project is intended to wrap the PostgreSQL datebase around using Python framework FastAPI to record my personal running training time. 

### Postman Documentation 
API documentation created using Postman, collection is available [here](https://documenter.getpostman.com/view/12154423/TW77g3o7).

### PostgreSQL Table 
The table contains the following field: 
- id
- distance
- intensity
- total time
- date

Should you want to add field in your table, you could modify the end point 'createTable' at main.py


## Development

Install development dependencies via:

```shell
poetry install
```

### Install poetry to Python
[Poetry](https://python-poetry.org) is a package manager for Python that utilises the latest `pyproject.tml`
project files.

`pyproject.tml` will eventually replace `setup.py` as the de facto standard
for managing and distribution Python projects.

Install poetry:
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

Check poetry is installed by displaying the help. The help is displayed by running:
```
poetry
```

After installing poetry, run:

```shell
poetry install --no-dev
```

Start the server with the following:

```shell
poetry run uvicorn src.server.main:app --reload
```

### Linting

Check linting:

```shell
poetry run flake8 src --statistics
```

Automatically fix linting issues:

```shell
poetry run autopep8 --in-place -r src
```
