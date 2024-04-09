from django.http.response import HttpResponseRedirect
from .models import *
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user:
            return self.request.user.usertype == 'editor' or self.request.user.usertype == 'admin'
        
    def handle_no_permission(self):
        return redirect(reverse_lazy('Users_app:user-login'))