from django.contrib import admin
from .models import Company, City, Internship

# Register your models here.
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("position",)}
