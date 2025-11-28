# from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from .models import *
from .forms import *


class AboutView(TemplateView):
    template_name = 'portfolio/about.html'


# def about(request):
#     return render(request, 'portfolio/about.html', )


class SkillsListView(ListView):
    model = Skill
    template_name = 'portfolio/skills.html'
    context_object_name = 'skills'


# def skills(request):
#     skills = Skill.objects.all()
#     return render(request, 'portfolio/skills.html', context={'skills': skills})


class ProjectsListView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'


# def projects(request):
#     projects = Project.objects.all()
#     return render(request, 'portfolio/projects.html', context={'projects': projects})

class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = 'portfolio/contact.html'
    success_url = reverse_lazy('about')

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('about')
#     else:
#         form = ContactForm()
#     return render(request, 'portfolio/contact.html', context={'form': form})
