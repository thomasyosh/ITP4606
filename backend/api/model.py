# from peewee import *
# import os
# import psycopg2

# db_type = os.getenv("DATABASE_TYPE")

# db_connection = None

# if db_type == "postgres":
    # db_connection = PostgresqlDatabase(
    #     'user',
    #     user=os.getenv("POSTGRES_USER"),
    #     host=os.getenv("POSTGRES_HOST"),
    #     password=os.getenv("POSTGRES_PASSWORD")
    #     )
# class MyUser (Model):
#    name=TextField()
#    age=IntegerField()
#    class Meta:
#       database=db_connection
#       db_table='MyUser'

# # db_connection.connect()
# # db_connection.create_tables([MyUser])




