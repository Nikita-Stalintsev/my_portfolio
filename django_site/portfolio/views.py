from django.shortcuts import render

def about(request):
    return render(request, 'portfolio/about.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def contacts(request):
    return render(request, 'portfolio/contacts.html')