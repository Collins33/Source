from django.contrib import admin
# Register your models here.
from .models import Editor,tags,Article

admin.site.register(Editor)
admin.site.register(tags)
admin.site.register(Article)
