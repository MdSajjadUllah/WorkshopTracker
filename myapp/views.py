from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User   
from .forms import SignupForm, SigninForm
from django.contrib.admin.views.decorators import staff_member_required


def landing(request):
    return render(request, "pages/landing.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  
            user.is_active = True           
            user.is_approved = False        
            user.save()
            messages.success(request, "Signup successful! Wait for admin approval before login.")
            return redirect("signin")
    else:
        form = SignupForm()
    return render(request, "pages/signup.html", {"form": form})


def signin(request):
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            try:
                # find user by email
                user_obj = User.objects.get(email=email)
                # authenticate
                user = authenticate(request, username=user_obj.username, password=password)
                if user is not None:
                    if not user.is_approved:
                        messages.error(request, "Your account is pending admin approval.")
                        return redirect("signin")
                    login(request, user)
                    return redirect("dashboard")
                else:
                    messages.error(request, "Invalid email or password.")
            except User.DoesNotExist:
                messages.error(request, "User not found.")
    else:
        form = SigninForm()
    return render(request, "pages/signin.html", {"form": form})


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("signin")
    return render(request, "pages/dashboard.html", {"user": request.user})


@staff_member_required
def approve_users(request):
    pending_users = User.objects.filter(is_approved=False)
    return render(request, "pages/approve_users.html", {"users": pending_users})


@staff_member_required
def approve_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_approved = True
    user.save()
    messages.success(request, f"{user.username} approved.")
    return redirect("approve_users")


@staff_member_required
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.success(request, "User deleted.")
    return redirect("approve_users")