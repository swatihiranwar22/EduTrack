from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import ApplicationForm


def home(request):
    return render(request, 'school/home.html')

def admission(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            return render(
                request,
                'school/success.html',
                {'application': application}
            )
    else:
        form = ApplicationForm()

    return render(
        request,
        'school/admission.html',
        {'form': form}
    )

def officer_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect("officer_dashboard")
    else:
        form = AuthenticationForm()

    return render(
        request,
        "school/login.html",
        {"form": form}
    )