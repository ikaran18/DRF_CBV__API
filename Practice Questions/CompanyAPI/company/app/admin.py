from django.contrib import admin
from .models import Company

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id','company_name','company_work','company_id','company_address']