# auto-generated snapshot
from peewee import *
import datetime
import model
import peewee


snapshot = Snapshot()


@snapshot.append
class Testing(peewee.Model):
    pk_id = AutoField(primary_key=True)
    Type = model.NullTextField(null=True)
    class Meta:
        table_name = "testing"


