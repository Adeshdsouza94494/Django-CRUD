from django.contrib import admin

from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone', 'branch') 

admin.site.register(Student, StudentAdmin)
