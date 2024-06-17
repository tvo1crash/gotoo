from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from gotoo.forms import ExtendedUserCreationForm
from gotoo.models import Course


def index(request):
    courses = Course.objects.distinct()
    return render(request, 'index.html', {'courses': courses})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def course_listings(request):
    courses = Course.objects.distinct()
    unique_course_count = Course.objects.values('title').distinct().count()
    return render(request, 'job-listings.html', {'courses': courses, 'unique_course_count': unique_course_count})


def course_details(request, course_id):
    courses = Course.objects.get(id=course_id)
    return render(request, 'course_details.html', {'courses': courses})

def registration(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data['email']
            user.email = email
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = ExtendedUserCreationForm()
    return render(request, 'registration.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    courses = Course.objects.filter(user=user)
    return render(request, 'profile.html', {'user': user, 'courses': courses})
