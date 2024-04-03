FROM python:3.12.2

WORKDIR /app

COPY requirements/backend.txt .
RUN pip install -r backend.txt --no-deps

COPY build build
COPY spaceship spaceship

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]