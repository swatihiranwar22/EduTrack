from django.db import models, transaction
from .grade import Grade
from .sequence import Sequence

class Application(models.Model):

    application_no = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_of_birth = models.DateField()
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    status_choices = [
        ('new', 'New'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    state = models.CharField(max_length=15, choices=status_choices, default='new')
    phone = models.CharField(max_length=15)
    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"Application {self.application_no} - {self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.application_no:
            with transaction.atomic():
                sequence = Sequence.objects.get(code='application')
                self.application_no = (
                    f"{sequence.prefix}{sequence.next_number:05d}"
                )

                sequence.next_number += 1
                sequence.save(update_fields=["next_number"])
        super().save(*args, **kwargs)
