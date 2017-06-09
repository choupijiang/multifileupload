from django.contrib import admin
from .models import DataTable, FileModel
# Register your models here.


class FileAdmin(admin.TabularInline):
    model = FileModel
    list_display = ['file']

class DataAdmin(admin.ModelAdmin):
    inlines = [FileAdmin,]
    list_display = ['id', 'name', ]

admin.site.register(DataTable, DataAdmin)