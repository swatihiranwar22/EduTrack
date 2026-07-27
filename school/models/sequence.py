from django.db import models

class Sequence(models.Model):
    code = models.CharField(max_length=50, unique=True)
    prefix = models.CharField(max_length=10)
    next_number = models.PositiveIntegerField(default=1)