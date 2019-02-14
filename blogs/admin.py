from django.contrib import admin
from .models import blog


class BlogAdmin(admin.ModelAdmin):
    model = blog
    prepopulated_fields = {'slug': ('title', )}

    class Media:
        js = ('ckeditor.js',)


admin.site.register(blog, BlogAdmin)
