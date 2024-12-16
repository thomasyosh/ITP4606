from peewee import *

class NullTextField(TextField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('null', True)
        super(NullTextField, self).__init__(*args, **kwargs)

class BaseModel(Model):
    pk_id = AutoField()
    
    @classmethod
    def fieldnames(cls) -> list[str]:
        return [f.name for f in cls.fields()]
    
    @classmethod
    def fields(cls) -> list[Field]:
        print("Override method for <BaseModel.fields> not implemented!")
        return []


class Testing(BaseModel):    
    Type = NullTextField()

class Student(BaseModel):
    ID = NullTextField()

