from django.db import models

# your models here


class Pokemon(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.TextField()
    photo = models.ImageField(null=True)

    def __str__(self):
        return '{}'.format(self.title)