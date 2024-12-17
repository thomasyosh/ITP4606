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
    modified_date = model.NullTextField(null=True)
    name = model.NullTextField(null=True)
    class Meta:
        table_name = "testing"


def forward(old_orm, new_orm):
    old_testing = old_orm['testing']
    testing = new_orm['testing']
    return [
        # Don't know how to do the conversion correctly, use the naive,
        testing.update({testing.modified_date: old_testing.modified_date}).where(old_testing.modified_date.is_null(False)),
    ]


def backward(old_orm, new_orm):
    testing = new_orm['testing']
    old_testing = old_orm['testing']
    return [
        # Apply default value datetime.datetime(2024, 12, 17, 0, 18, 24, 738425) to the field testing.modified_date,
        testing.update({testing.modified_date: datetime.datetime(2024, 12, 17, 0, 18, 24, 738425)}).where(testing.modified_date.is_null(True)),
        # Don't know how to do the conversion correctly, use the naive,
        testing.update({testing.modified_date: old_testing.modified_date}).where(old_testing.modified_date.is_null(False)),
    ]
