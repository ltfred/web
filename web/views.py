from django.shortcuts import render


def page_not_found(request, exception, template_name='error_page.html'):
    return render(request, template_name, {"code": 404, "msg": "Sorry! 页面找不到了"})


def server_error(request, exception, template_name='error_page.html'):
    return render(request, template_name, {"code": 500, "msg": "Sorry! 服务器出了点问题"})