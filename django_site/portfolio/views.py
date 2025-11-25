from django.shortcuts import render, redirect
from .models import *
from .forms import *


def about(request):
    return render(request, 'portfolio/about.html', )


def skills(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio/skills.html', context={'skills': skills})


def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', context={'projects': projects})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', context={'form': form})
