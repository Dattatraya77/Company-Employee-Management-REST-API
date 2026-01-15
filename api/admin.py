from django.contrib import admin
from .models import Company, Employee


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["company_id", "name", "location", "about", "company_type", "created_at", "updated_at", "active"]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "address", "phone", "about", "employee_position", "company", "created_at", "updated_at", "active"]