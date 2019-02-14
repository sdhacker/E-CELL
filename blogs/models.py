from django.db import models
from ckeditor.fields import RichTextField

class blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = RichTextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:150]+"..."
