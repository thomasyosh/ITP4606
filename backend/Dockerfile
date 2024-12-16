FROM python:latest

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN [ "pip", "install", "-r", "requirements.txt" ]

COPY --chmod=0777 ./db/init.sh /docker-entrypoint-initdb.d/init.sh

COPY api /app/api/

CMD [ "fastapi", "run", "api/main.py" ]