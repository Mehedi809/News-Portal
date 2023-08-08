from django.contrib import admin
from .models import *

# Register your models here.
DataTable = [Banner, Category, Content]
admin.site.register(DataTable)
