from django.contrib import admin

# Register your models here.
from .models import Grade, Application, Sequence, Student
admin.site.register(Grade)
admin.site.register(Application)
admin.site.register(Sequence)
admin.site.register(Student)