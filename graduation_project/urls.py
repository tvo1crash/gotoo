from django.shortcuts import render

from gotoo import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404, handler500


def custom_page_not_found_view(request, exception):
    return render(request, "404.html", {})


def custom_error_view(request):
    return render(request, "500.html", {})


urlpatterns = [
    path('', views.index, name='index'),
    path('cause-error/', views.cause_error),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('listings', views.course_listings, name='listings'),
    path('registration/', views.registration, name='registration'),
    path('', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('course/<int:pk>/add/', views.add_course_to_user, name='add_course_to_user'),

]

handler404 = custom_page_not_found_view
handler500 = custom_error_view
