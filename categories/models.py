from django.db import models
from dbs.base.models import BaseModel

class Categories(BaseModel):
    display_name = models.CharField(max_length=400)
