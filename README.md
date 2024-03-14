### Automated Testing in Python (pytest, flake8, mypy, tox and GitHub Actions)

[![Tests](https://github.com/dsuprunov/python-automated-testing/actions/workflows/tests.yml/badge.svg)](https://github.com/dsuprunov/python-automated-testing/actions/workflows/tests.yml)
[![Docker](https://github.com/dsuprunov/python-automated-testing/actions/workflows/docker.yml/badge.svg)](https://github.com/dsuprunov/python-automated-testing/actions/workflows/docker.yml)

This repository utilizes a custom Docker image based on Ubuntu 22.04 LTS, which incorporates three versions of Python: 3.12, 3.11, and 3.10. The image is derived from `dsuprunov/python-multi-version:latest`. This custom Docker image enables running tests across all three Python versions seamlessly using `tox`.

#### Running Tests Across All Python Versions
To run tests across all Python versions (3.12, 3.11, and 3.10), use the custom Docker image specified in the Dockerfile:

```Dockerfile
FROM dsuprunov/python-multi-version:latest
```

Then, execute your tests with tox.

#### Testing in Specific Python Version
If you only need to test in a specific Python version, you can switch to a base Python image for that version. For example, to test in Python 3.12:

```Dockerfile
FROM python:3.12-slim
```
Adjust the Dockerfile as necessary for the specific Python version you require.


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

tox
```bash
tox
```

#### Building and running Docker

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

#### Building and running in Docker Compose

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