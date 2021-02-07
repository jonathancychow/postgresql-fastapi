# python-postgressql-poke-around

Folloing instruction on this [link](https://stackabuse.com/working-with-postgresql-in-python/)

Useful SQL syntax and youtube [link](https://www.youtube.com/watch?v=5tEApCGgpEQ&ab_channel=BecomingaDataScientist) 
 - SELECT * FROM student
 - UPDATE STUDENT set AGE = 20 where ADMISSION = 3420 
 - DELETE from STUDENT where ADMISSION=3420



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
poetry run uvicorn src.server.main:app
```

## Development

Install development dependencies via:

```shell
poetry install
```

Use the `--reload` flag:

```
poetry run uvicorn src.mat.sim.rFPro.main:app --reload
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
