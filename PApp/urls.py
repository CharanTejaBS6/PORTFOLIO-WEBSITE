from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),
    path('achievements/', views.achievements, name='achievements'),
    path('send-email/', views.send_email, name='send_email'),
    path('about-me/', views.about , name='about'),
]
