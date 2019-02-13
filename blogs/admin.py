from django.contrib import admin
from .models import blog


class BlogAdmin(admin.ModelAdmin):
    model = blog
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(blog, BlogAdmin)
