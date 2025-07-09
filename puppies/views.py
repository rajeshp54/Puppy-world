from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse

from .models import Puppy
from .forms import PuppyForm



@login_required
def home(request):
    return render(request, 'puppies/home.html')


@login_required
def add_puppy(request):
    if request.method == 'POST':
        form = PuppyForm(request.POST, request.FILES)
        if form.is_valid():
            puppy = form.save(commit=False)
            puppy.owner = request.user
            puppy.save()
            messages.success(request, "Thanks for your details! Puppy added successfully.")
            return redirect('puppy_list')
        return render(request, 'add_puppy.html')
    else:
        form = PuppyForm()

    return render(request, 'puppies/puppy_form.html', {'form': form})


@login_required(login_url='/login/')
def list_puppies(request):
    query = request.GET.get('q')
    if query:
        puppies = Puppy.objects.filter(
            breed__icontains=query
        )
    else:
        puppies = Puppy.objects.all()

    return render(request, 'puppies/puppy_list.html', {'puppies': puppies})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have signed successfully! 🎉')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class CustomLoginView(LoginView):
    def get_success_url(self):
        return '/'


from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Puppy

@login_required
def live_search(request):
    query = request.GET.get('q', '')
    puppies = Puppy.objects.filter(breed__icontains=query)

    results = []
    for puppy in puppies:
        results.append({
            'breed': puppy.breed,
            'age_year': puppy.age_year,
            'age_month': puppy.age_month,
            'location': puppy.location,
            'contact': puppy.contact,
            'image_url': puppy.image.url if puppy.image else '', 
        })

    return JsonResponse({'results': results})

def custom_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")  
    return redirect('login')
