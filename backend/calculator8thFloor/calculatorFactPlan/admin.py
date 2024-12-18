from django.contrib import admin
from .models import Data, TableColumnName, LastPasswordChangeDate

# Register your models here.

admin.site.register(Data)
admin.site.register(TableColumnName)
admin.site.register(LastPasswordChangeDate)
