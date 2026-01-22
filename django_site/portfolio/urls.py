from django.urls import path
from .views import *

urlpatterns = [
    path('', AboutView.as_view(), name="about"),
    path('skills/', SkillsListView.as_view(), name="skills"),
    path('projects/', ProjectsListView.as_view(), name="projects"),
    path('contact/', ContactCreateView.as_view(), name="contact"),
]
