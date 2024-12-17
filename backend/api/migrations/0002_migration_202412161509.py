# auto-generated snapshot
from peewee import *
import datetime
import model
import peewee


snapshot = Snapshot()


@snapshot.append
class Testing(peewee.Model):
    pk_id = AutoField(primary_key=True)
    created_date = DateTimeField(default=datetime.datetime.now)
    Type = model.NullTextField(null=True)
    class Meta:
        table_name = "testing"


def forward(old_orm, new_orm):
    testing = new_orm['testing']
    return [
        # Apply default value datetime.datetime(2024, 12, 16, 15, 9, 27, 334404) to the field testing.created_date,
        testing.update({testing.created_date: datetime.datetime(2024, 12, 16, 15, 9, 27, 334404)}).where(testing.created_date.is_null(True)),
    ]
