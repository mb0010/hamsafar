
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import User
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

def home(request):
    trips = Trip.objects.all()  
    return render(request, 'home.html', {'trips': trips})

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required 
def add_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.user = request.user  
            trip.save()
            return redirect('view_trips')
    else:
        form = TripForm()  
    
    return render(request, 'add_trip.html', {'form': form})



def delete_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, user=request.user)
    trip.delete()
    return redirect('view_trips')

def view_trips(request):
    trips = Trip.objects.all()
    return render(request, 'view_trips.html', {'trips': trips})

def add_companion_request(request):
    if request.method == 'POST':
        form = CompanionRequestForm(request.POST)
        if form.is_valid():
            companion_request = form.save(commit=False)
            companion_request.user = request.user
            companion_request.save()
            return redirect('view_companion_requests')
    else:
        form = CompanionRequestForm()
    return render(request, 'add_companion_request.html', {'form': form})

def delete_companion_request(request, request_id):
    companion_request = get_object_or_404(CompanionRequest, id=request_id, user=request.user)
    companion_request.delete()
    return redirect('view_companion_requests')

def view_companion_requests(request):
    companion_requests = CompanionRequest.objects.all()
    return render(request, 'view_companion_requests.html', {'companion_requests': companion_requests})

from django.shortcuts import render, redirect, get_object_or_404
from .forms import TripForm, CompanionRequestForm
from .models import Trip, CompanionRequest


def update_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('view_trips')
    else:
        form = TripForm(instance=trip)
    return render(request, 'update_trip.html', {'form': form})


def delete_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    if request.method == 'POST':
        trip.delete()
        return redirect('view_trips')
    return render(request, 'confirm_delete_trip.html', {'trip': trip})


def update_companion_request(request, request_id):
    companion_request = get_object_or_404(CompanionRequest, id=request_id)
    if request.method == 'POST':
        form = CompanionRequestForm(request.POST, instance=companion_request)
        if form.is_valid():
            form.save()
            return redirect('view_companion_requests')
    else:
        form = CompanionRequestForm(instance=companion_request)
    return render(request, 'update_companion_request.html', {'form': form})


def delete_companion_request(request, request_id):
    companion_request = get_object_or_404(CompanionRequest, id=request_id)
    if request.method == 'POST':
        companion_request.delete()
        return redirect('view_companion_requests')
    return render(request, 'confirm_delete_companion_request.html', {'companion_request': companion_request})
def view_companion_request_detail(request, id):
    # Fetch the specific companion request or return a 404 if not found
    request_detail = get_object_or_404(CompanionRequest, id=id)
    return render(request, 'view_companion_request_detail.html', {'request': request_detail})
def edit_companion_request(request, id):
    companion_request = get_object_or_404(CompanionRequest, id=id)

    if request.method == 'POST':
        form = CompanionRequestForm(request.POST, instance=companion_request)
        if form.is_valid():
            form.save()
            return redirect('view_companion_requests')  # Redirect to the list of companion requests
    else:
        form = CompanionRequestForm(instance=companion_request)

    return render(request, 'edit_companion_request.html', {'form': form, 'companion_request': companion_request})
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Trip

def view_trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    return render(request, 'view_trip_detail.html', {'trip': trip})
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Trip
from .forms import TripForm  # Assume you have a form for updating trips

# View for showing trip details
def view_trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    return render(request, 'view_trip_detail.html', {'trip': trip})

# View for updating trip
def update_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)  # Ensure this line correctly fetches the trip object
    
    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('view_trip_detail', trip_id=trip.id)  # Correct use of trip.id
    else:
        form = TripForm(instance=trip)
    
    return render(request, 'update_trip.html', {'form': form, 'trip': trip})
# View for deleting trip
def delete_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    
    if request.method == 'POST':
        trip.delete()
        return redirect('view_trips')  # Redirect to the list of trips
    
    return render(request, 'delete_trip_confirmation.html', {'trip': trip})
