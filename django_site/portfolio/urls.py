from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name="about"),
    path('skills/', views.skills, name="skills"),
    path('projects/', views.projects, name="projects"),
    path('contact/', views.contact, name="contact"),
]
