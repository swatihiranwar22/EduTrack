from django.db import models
from .application import Application
from .grade import Grade
from .sequence import Sequence

class Student(models.Model):
    student_no = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
        blank=True
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    application = models.OneToOneField(
        Application,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student_no} - {self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.student_no:
            sequence = Sequence.objects.get(code='student')
            self.student_no = f"{sequence.prefix}{sequence.next_number:05d}"

            sequence.next_number += 1
            sequence.save(update_fields=["next_number"])
        super().save(*args, **kwargs)