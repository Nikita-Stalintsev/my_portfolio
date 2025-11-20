from django.shortcuts import render

nav_buttons = [
    {'title': 'ОБО МНЕ', 'url_name': 'about', 'path': '/'},
    {'title': 'НАВЫКИ', 'url_name': 'skills', 'path': '/skills/'},
    {'title': 'ПРОЕКТЫ', 'url_name': 'projects', 'path': '/projects/'},
    {'title': 'КОНТАКТЫ', 'url_name': 'contacts', 'path': '/contacts/'},
]
context = {
    'nav_buttons': nav_buttons,
}

def about(request):
    return render(request, 'portfolio/about.html', context=context)

def skills(request):
    return render(request, 'portfolio/skills.html', context=context)

def projects(request):
    return render(request, 'portfolio/projects.html', context=context)

def contacts(request):
    return render(request, 'portfolio/contacts.html', context=context)