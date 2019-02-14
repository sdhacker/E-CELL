from django.db import models

class gallery(models.Model):
    index = models.PositiveIntegerField()
    desciption = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    def __int__(self):
        return self.index
