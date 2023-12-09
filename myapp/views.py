from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, RecruiterProfile
from .forms import UserProfileForm
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the custom login page
            return redirect('custom_login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)

                # Check if the user has a profile
                user_profile = UserProfile.objects.filter(user=user).first()
                if user_profile is None:
                    # If no profile exists, redirect to create_profile
                    return redirect('create_profile')
                else:
                    # Otherwise, redirect to profile_detail
                    return redirect('profile_detail')
            else:
                # Handle authentication failure
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid login credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile_detail(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'profile_detail.html', {'user_profile': user_profile})

@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('profile_detail')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'form': form})

@login_required
def create_profile(request):
    # Check if the user already has a profile
    existing_profile = UserProfile.objects.filter(user=request.user).first()

    if existing_profile:
        # Redirect to profile_detail if a profile already exists
        return redirect('profile_detail')

    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('profile_detail')
    else:
        form = UserProfileForm()

    return render(request, 'create_profile.html', {'form': form})






from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RecruiterSignupForm

# Existing views...

def recruiter_signup(request):
    if request.method == 'POST':
        form = RecruiterSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)

            recruiter_profile = RecruiterProfile(user=user, company=form.cleaned_data['company'])
            recruiter_profile.save()

            return redirect('recruiter_dashboard')
    else:
        form = RecruiterSignupForm()
    return render(request, 'recruiter_signup.html', {'form': form})

def recruiter_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)

                # Redirect to the recruiter dashboard
                return redirect('recruiter_dashboard')
            else:
                # Handle authentication failure
                return render(request, 'recruiter_login.html', {'form': form, 'error_message': 'Invalid login credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'recruiter_login.html', {'form': form})

# myapp/views.py
from django.shortcuts import render
from .models import UserProfile, RecruiterProfile
from django.contrib.auth.decorators import login_required

@login_required
def recruiter_dashboard(request):
    # Exclude the recruiter's own profile
    recruiter_profile = RecruiterProfile.objects.get(user=request.user)
    other_user_profiles = UserProfile.objects.exclude(user=request.user)

    return render(request, 'recruiter_dashboard.html', {'recruiter_profile': recruiter_profile, 'other_user_profiles': other_user_profiles})

