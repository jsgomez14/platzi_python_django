""" Users views """

#Django
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Exceptions
from django.db.utils import IntegrityError

# Forms
from users.forms import ProfileForm, SignupForm

@login_required
def update_profile(request):
    """Updates a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')
    else:
        form = ProfileForm()

    return render(
        request,
        'users/update_profile.html',
        context = {
            'profile':profile,
            'user': request.user,
            'form': form
        })

def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
    return render(request, 'users/login.html')

def signup_view(request):
    """Signup view."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()   
    return render(
        request = request,
        template_name= 'users/signup.html',
        context= {'form':form})

    
@login_required
def logout_view(request):
    """Logout view."""
    logout(request)
    return redirect('login')