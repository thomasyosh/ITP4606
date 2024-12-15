FROM python:latest

WORKDIR /app

COPY api /app/api/

COPY ./requirements.txt /app/requirements.txt

RUN [ "pip", "install", "-r", "requirements.txt" ]

CMD ["fastapi", "run", "api/main.py"]