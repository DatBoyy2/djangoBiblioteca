from django.shortcuts import render
from django.views.generic.edit import UpdateView 
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book 
from .forms import BookForm 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Users.helpers import *
from django.db.models import Q

#modificar views

class BookUpdateView(StaffRequiredMixin, UpdateView): 
	# specify the model you want to use 
	model = Book 
	template_name = "update.html"
	# specify the fields 
	fields = [ 
        "title",
        "author",
        "year" ,
        "theme",
        "ISBN",
        "SBM",
        "editorial",
        "plot" 
    ]

	success_url ="/"
	login_url= reverse_lazy('Users_app:user-login')
     
@login_required(login_url='/login/')

def create_view(request): 
    context ={} 

    form = BookForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 

    context['form']= form 
    return render(request, "createBook.html", context) 

def list_view(request):
    context = {}

    if 'query' in request.GET:
        query = request.GET.get('query')
        libros = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__name__icontains=query) |
            Q(theme__name__icontains=query) |
            Q(ISBN__icontains=query)
        )
        context['query'] = query
        context['dataset'] = libros
    else:
        context['dataset'] = Book.objects.all()

    return render(request, "list.html", context)

def libro_detail(request, libro_id):
    libro = Book.objects.get(pk=libro_id)
    
    return render(request, 'libro-detail.html', {'libro': libro})