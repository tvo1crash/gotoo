from gotoo import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('listings', views.course_listings, name='listings'),
    path('registration/', views.registration, name='registration'),
    path('', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('course/<int:pk>/add/', views.add_course_to_user, name='add_course_to_user')
]
