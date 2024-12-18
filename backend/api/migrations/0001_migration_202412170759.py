# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class User(peewee.Model):
    pk_id = AutoField(primary_key=True)
    created_date = DateTimeField(default=datetime.datetime.now)
    modified_date = DateTimeField(null=True)
    is_active = BooleanField(default=True)
    name = TextField(null=True)
    telephone = TextField(null=True)
    password = TextField(null=True)
    class Meta:
        table_name = "user"


def migrate_forward(op, old_orm, new_orm):
    op.create_table(new_orm.user)
    op.run_data_migration()


def migrate_backward(op, old_orm, new_orm):
    op.run_data_migration()
    op.drop_table(old_orm.user)
