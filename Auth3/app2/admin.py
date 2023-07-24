from django.contrib import admin
from app2.models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','address','phone','city']
