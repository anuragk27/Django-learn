from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages

def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Sign Up Successful')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request,'enroll_app/signup.html',{'form':fm})