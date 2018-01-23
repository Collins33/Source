from django.contrib import admin
# Register your models here.
from .models import tags,Article

class ArticleAdmin(admin.ModelAdmin):
     filter_horizontal =('tags',)


admin.site.register(tags)
admin.site.register(Article,ArticleAdmin)
