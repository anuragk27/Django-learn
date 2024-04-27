from django.shortcuts import render , HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Signup view function
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Sign Up Successful')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request,'app/signup.html',{'form':fm})

# Login view function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request = request,data=request.POST)

            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname, password = upass)

                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully')
                    return HttpResponseRedirect('/profile/')
    
        else:
            fm = AuthenticationForm()
        return render(request,'app/userlogin.html',{'form':fm})

    else:
        return HttpResponseRedirect('/profile/')

# profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'app/profile.html', {'name':request.user})
    else:
        return HttpResponseRedirect('/login/')

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#Change Password with Old pass
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user = request.user, data = request.POST)

            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)

                messages.success(request,'Password Change Successful')
                return HttpResponseRedirect('/profile/')
        
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request,'app/changepass.html',{'form':fm})

    else:
        return HttpResponseRedirect('/login/')