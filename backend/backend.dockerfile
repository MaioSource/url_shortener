FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app/

COPY ./app /app

RUN pip install -r requirements.txt

ENV PYTHONPATH=/app

