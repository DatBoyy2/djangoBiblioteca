from django.urls import path 
	
from .views import *
app_name= 'Biblioteca_app'
urlpatterns = [ 
	path('libro/<int:pk>/', BookUpdateView.as_view(), name="libro-update"), 
    path('create', create_view, name="create_view"),
    path('', list_view, name='list'),
    path('libro-detalle/<int:libro_id>/', libro_detail, name='libro-detail'),
] 

