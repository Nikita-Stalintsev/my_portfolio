from django.shortcuts import render
from .models import *


def about(request):
    return render(request, 'portfolio/about.html', )


def skills(request):
    skill_objs = Skills.objects.all()

    return render(request, 'portfolio/skills.html', context={'skills': skill_objs})


def projects(request):
    return render(request, 'portfolio/projects.html', )


def contacts(request):
    return render(request, 'portfolio/contacts.html', )
