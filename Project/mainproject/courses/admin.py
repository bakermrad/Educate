from django.contrib import admin

# Register your models here.

from .models import Course, Major

admin.site.register(Course)
admin.site.register(Major)