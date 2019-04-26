from django.contrib import admin

# Register your models here.
#this is sanath
from .models import Todo
class TodoAdmin(admin.ModelAdmin):
    list_display=('id','title','description','completed')
    admin.site.register(Todo)
