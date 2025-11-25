def nav_buttons(request):
    return {
        'nav_buttons': [
            {'title': 'ОБО МНЕ', 'url_name': 'about', 'path': '/'},
            {'title': 'НАВЫКИ', 'url_name': 'skills', 'path': '/skills/'},
            {'title': 'ПРОЕКТЫ', 'url_name': 'projects', 'path': '/projects/'},
            {'title': 'КОНТАКТЫ', 'url_name': 'contact', 'path': '/contact/'},
        ]
    }
