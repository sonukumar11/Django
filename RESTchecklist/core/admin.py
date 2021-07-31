from django.contrib import admin
from .models import CheckList , CheckListItem

# Register your models here.
admin.site.register(CheckList)
admin.site.register(CheckListItem)