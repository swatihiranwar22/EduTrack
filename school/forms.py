from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application

        fields = [
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "gender",
            "phone",
            "father_name",
            "mother_name",
            "grade",
            "remarks",
        ]