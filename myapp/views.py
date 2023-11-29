from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm

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
def profile_detail(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
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
