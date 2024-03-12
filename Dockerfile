FROM python:3.12-slim

FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src
COPY ./tests ./tests

CMD ["python3", "src/main.py"]