from django.db import models

# your models here


class Pokemon(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.TextField()
