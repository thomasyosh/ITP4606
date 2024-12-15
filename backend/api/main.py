from fastapi import FastAPI
import os
from peewee import *
import psycopg2
import pymysql

app = FastAPI(title=os.getenv("PROJECT_NAME"))

db_type = os.getenv("DATABASE_TYPE")

if db_type == "postgres":
    db_connection = PostgresqlDatabase(
        'user',
        user=os.getenv("POSTGRES_USER"),
        host=os.getenv("POSTGRES_HOST"),
        password=os.getenv("POSTGRES_PASSWORD")
        )
elif db_type == "mysql":
    db_connection = MySQLDatabase(
        "testing",
        user="root",
        host="mysql",
        password=os.getenv("MYSQL_ROOT_PASSWORD")
    )

class MyUser (Model):
   name=TextField()
   age=IntegerField()
   class Meta:
      database=db_connection
      db_table='MyUser'

db_connection.connect()
db_connection.create_tables([MyUser])

@app.get("/")
async def root():
    # environ = os.getenv("DOCKER_DATABASE_URL")
    return {"message": "hi"}