# Base image
FROM python:3.12

WORKDIR /FastAPI_main

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock* ./

# IMPORTANT LINE
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
