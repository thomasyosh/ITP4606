from fastapi import FastAPI, Form
import os
from peewee import *
import psycopg2
import pymysql
from model import Testing, BaseModel
from post_item import Item, FormData
from typing import Annotated

app = FastAPI(title=os.getenv("PROJECT_NAME"))

@app.get("/")
async def root():
    query = Testing.select().dicts()
    return list(query)

@app.get("/testing/{item_id}")
async def read_item(item_id: str | None = None):
    query = Testing().select().where(Testing.pk_id == item_id).dicts().get()
    return query

@app.post("/testing")
async def root(item: Item):
    data = Testing()
    data.name = item.name
    data.save()
    return {"message": "こんにちは"}

@app.put("/update")
async def update_record(data: Annotated[FormData, Form()]) -> None:
    update_data = Testing().update({Testing.name:data.name}).where(Testing.pk_id == data.pk_id)
    update_data.execute()
    query = Testing().select().where(Testing.pk_id == data.pk_id).dicts().get()
    return query