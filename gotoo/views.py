from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from gotoo.forms import ExtendedUserCreationForm, AvatarForm
from gotoo.models import Course, Profile


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


@login_required
def add_course_to_user(request, pk):
    course = get_object_or_404(Course, pk=pk)
    user = request.user
    user.courses.add(course)
    return redirect('course_detail', pk=pk)


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course_details.html', {'course': course})


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
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AvatarForm(instance=profile)

    courses = user.courses.all()
    context = {
        'user': user,
        'courses': courses,
        'form': form,
    }
    return render(request, 'profile.html', context)