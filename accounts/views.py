from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UserUpdateForm


# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('product_list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})



@login_required
def profile(request):
    user_profile = request.user.profile
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=user_profile)
        user_form = UserUpdateForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'profile_form': profile_form, 'user_form': user_form, 'profile': user_profile})