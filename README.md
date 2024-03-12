### Automated Testing in Python

[![Tests](https://github.com/dsuprunov/python-automated-testing/actions/workflows/tests.yml/badge.svg)](https://github.com/dsuprunov/python-automated-testing/actions/workflows/tests.yml)

- pytest
- flake8
- tox
- mypy
- GitHub Actions

#### Usage

```bash
pytest -v
```

```bash
flake8 src tests
```

```bash
mypy src
```

tox (python3.12) + (pytest, flake8, mypy)
```bash
tox
```

#### Docker

Build image
```bash
docker build . -t python-automated-testing-app:latest
```

Run app in the container
```bash
docker run --rm python-automated-testing-app:latest
```

Run shell/bash in the container 
```bash
docker run -ti --rm python-automated-testing-app:latest bash
```

#### Docker Compose

Build image
```bash
docker-compose build
```

Run app in the container
```bash
docker-compose run app
```

Run shell/bash in the container 
```bash
docker-compose run app bash
```