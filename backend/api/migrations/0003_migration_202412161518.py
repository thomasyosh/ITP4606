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
    modified_date = DateTimeField()
    Type = model.NullTextField(null=True)
    class Meta:
        table_name = "testing"


def forward(old_orm, new_orm):
    testing = new_orm['testing']
    return [
        # Apply default value datetime.datetime(2024, 12, 16, 15, 18, 17, 194289) to the field testing.modified_date,
        testing.update({testing.modified_date: datetime.datetime(2024, 12, 16, 15, 18, 17, 194289)}).where(testing.modified_date.is_null(True)),
    ]


def migrate_forward(op, old_orm, new_orm):
    op.add_column(new_orm.testing.modified_date)
    op.run_data_migration()
    op.add_not_null(new_orm.testing.modified_date)


def migrate_backward(op, old_orm, new_orm):
    op.run_data_migration()
    op.drop_column(old_orm.testing.modified_date)
