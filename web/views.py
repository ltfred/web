from django.shortcuts import render



def page_not_found(request, exception, template_name='404_page.html'):
    return render(request, template_name)

def server_error(request, exception, template_name='500_page.html'):
    return render(request, template_name)