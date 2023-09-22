from django.db import models
from accounts.models import CustomUser
from categories.models import Categories
from dbs.base.models import BaseModel

class Post(BaseModel):
    title = models.CharField(max_length=400)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

