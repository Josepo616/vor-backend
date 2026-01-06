# Lightweight python image
FROM python:3.11-slim

# Avoid generation of files .pyc and exit buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies to compile drivers and libraries (optional but recommended)
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# install poetry
RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* /app/

# Deny poetry to create virtualenvs (this is an isolated container)
RUN poetry install --no-root --no-interaction --no-ansi

# Copy rest of code
COPY . /app

# expose the port
EXPOSE 8000

# Comannd to run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]