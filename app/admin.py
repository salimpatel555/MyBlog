from django.contrib import admin
from.models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['user','title','description','creat_at','updated_at']
admin.site.register(Blog,BlogAdmin)
