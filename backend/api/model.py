from peewee import *
import os
import datetime

class NullTextField(TextField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('null', True)
        super(NullTextField, self).__init__(*args, **kwargs)

class BaseModel(Model):
    pk_id = AutoField()
    created_date = DateTimeField(default=datetime.datetime.now)
    modified_date = DateTimeField(null = True)

    @classmethod
    def update(cls, *args, **kwargs):
        kwargs["modified_date"] = datetime.datetime.now()
        return super(BaseModel,cls).update(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.created_date = datetime.datetime.now()
        return super(BaseModel,self).save(*args, **kwargs)
    
    @classmethod
    def fieldnames(cls) -> list[str]:
        return [f.name for f in cls.fields()]
    
    @classmethod
    def fields(cls) -> list[Field]:
        print("Override method for <BaseModel.fields> not implemented!")
        return []


class Testing(BaseModel):    
    name = NullTextField()

class Student(BaseModel):
    ID = NullTextField()

db_type = os.getenv("DATABASE_TYPE")

if db_type == "postgres":
    db_connection = PostgresqlDatabase(
        os.getenv("POSTGRES_DB"),
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

Testing.bind(db_connection)
db_connection.connect()
db_connection.create_tables([Testing])

