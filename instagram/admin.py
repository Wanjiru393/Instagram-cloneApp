from django.contrib import admin

# Register your models here.

from .models import Post, Tag, Follow

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Follow)
