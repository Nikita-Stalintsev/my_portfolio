from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from .models import Skill, Project
from .forms import ContactForm


class AboutView(TemplateView):
    template_name = 'portfolio/about.html'


class SkillsListView(ListView):
    model = Skill
    template_name = 'portfolio/skills.html'
    context_object_name = 'skills'


class ProjectsListView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'


class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = 'portfolio/contact.html'
    success_url = reverse_lazy('about')

