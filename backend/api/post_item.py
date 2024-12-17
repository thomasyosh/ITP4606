from pydantic import BaseModel, Field
import datetime

class Item(BaseModel):
    name: str = Field(default='John Doe')
    
    
class FormData(BaseModel):
    pk_id: str
    name: str
    model_config = {"extra": "forbid"}