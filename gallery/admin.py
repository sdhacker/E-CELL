from django.contrib import admin
from .models import gallery


class Gallery(admin.ModelAdmin):
    model = gallery


admin.site.register(gallery, Gallery)


