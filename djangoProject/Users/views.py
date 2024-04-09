from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import *
from django.views.generic import View, FormView

from django.views.generic import(
    View,
)
from django.views.generic.edit import(
    FormView,
    UpdateView
)
from .forms import LoginForm


class LoginUser(FormView):
    template_name= 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('Biblioteca_app:list')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)
    
class LogoutUser(View):
    def get(elf,request,*args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'Users_app:user-login'
            )
        )
        
class CreateUser(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('Users_app:user-login')

    def form_valid(self, form):
        usuario = User.objects.create_user(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            name=form.cleaned_data['name'],
            surname=form.cleaned_data['surname'],
            usertype='VIEW',
            is_active=True,
        )
        return super().form_valid(form)

