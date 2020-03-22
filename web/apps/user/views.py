from django import http
from django.contrib.auth import login
from django.shortcuts import render
from django.views import View
from user.models import Users



class LoginView(View):

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Users.objects.get(username=username)
        except:
            return http.JsonResponse({'code': 400, 'msg': '用户名或密码错误'})
        if not user.check_password(password):
            return http.JsonResponse({'code': 400, 'msg': '用户名或密码错误'})
        login(request,user)
        return http.JsonResponse({'code': 200})