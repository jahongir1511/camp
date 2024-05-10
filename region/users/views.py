from django.shortcuts import render
from django.views import View

class RegisterView(View):
    def get(self, request):
        return render(request, template_name='register.html')


class LoginView(View):
    def get(self, request):
        return render(request, template_name='login.html')
