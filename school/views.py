from django.shortcuts import render
from .forms import ApplicationForm

# Create your views here.
def home(request):
    return render(request, 'school/home.html')

def admission(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            return render(
                request, 'school/admission_success.html', {'application': application}
            )
    else:
        form = ApplicationForm()
        return render(request, 'school/admission.html', {'form': form})
    return render(request, 'school/admission.html', {'form': form})