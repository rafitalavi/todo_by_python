from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm ,AdminPasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from roleapp.models import Role
from django import forms
from django.contrib.auth.decorators import user_passes_test
from .forms import CustomUserCreationForm, UserProfileForm,CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash


def superuser_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_active and u.is_superuser)(view_func)
    return decorated_view_func    
@superuser_required  
# Forms for UserProfile fields




@superuser_required
def create_user(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.email = user_form.cleaned_data['email']
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('user_list')
    else:
        user_form = CustomUserCreationForm()
        profile_form = UserProfileForm()

    return render(request, 'userapp/user_form.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

# Edit user + profile view

from .forms import CustomUserChangeForm  # create this form similar to CustomUserCreationForm but for editing

@superuser_required  
def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('userapp:user_detail', user_id=user.id)
    else:
        user_form = CustomUserChangeForm(instance=user)
        profile_form = UserProfileForm(instance=profile)

    return render(request, 'userapp/user_form.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


# User detail view
@login_required
@superuser_required  
def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    profile = UserProfile.objects.filter(user=user).first()
    return render(request, 'userapp/user_detail.html', {
        'user': user,
        'profile': profile,
    })


# Optionally: List all users (for admin or superuser)
@login_required
@superuser_required  
def user_list(request):
    users = User.objects.all().select_related('userprofile')
    return render(request, 'userapp/user_list.html', {
        'users': users,
    })
@superuser_required
def change_password(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = AdminPasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user)  # Important to keep session
            return redirect('userapp:user_detail', user_id=user.id)
    else:
        form = AdminPasswordChangeForm(user)
    return render(request, 'userapp/change_password.html', {'form': form, 'user': user})
