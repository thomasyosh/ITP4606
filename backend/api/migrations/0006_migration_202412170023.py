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
    modified_date = DateTimeField(null=True)
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


def migrate_forward(op, old_orm, new_orm):
    op.rename_column(old_orm.testing.modified_date, 'old__modified_date')
    op.add_column(new_orm.testing.modified_date)
    op.run_data_migration()
    op.drop_column(old_orm.testing.modified_date)


def backward(old_orm, new_orm):
    old_testing = old_orm['testing']
    testing = new_orm['testing']
    return [
        # Don't know how to do the conversion correctly, use the naive,
        testing.update({testing.modified_date: old_testing.modified_date}).where(old_testing.modified_date.is_null(False)),
    ]


def migrate_backward(op, old_orm, new_orm):
    op.rename_column(old_orm.testing.modified_date, 'old__modified_date')
    op.add_column(new_orm.testing.modified_date)
    op.run_data_migration()
    op.drop_column(old_orm.testing.modified_date)
