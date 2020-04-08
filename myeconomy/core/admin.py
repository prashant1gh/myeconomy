from django.contrib import admin
from .models import DailyTransaction, Category
from import_export.admin import ImportExportModelAdmin


class DailyTransactionAdmin(ImportExportModelAdmin):
    list_display = ['date', 'inc_exp', 'category', 'amount']
    
admin.site.register(DailyTransaction, DailyTransactionAdmin)
admin.site.register(Category)