from django.shortcuts import render
from .models import *


def about(request):
    return render(request, 'portfolio/about.html', )


def skills(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio/skills.html', context={'skills': skills})


def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', context={'projects': projects})


def contacts(request):
    return render(request, 'portfolio/contacts.html', )
