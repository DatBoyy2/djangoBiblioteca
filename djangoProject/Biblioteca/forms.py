from django import forms 
from .models import Book 


class BookForm(forms.ModelForm): 

    class Meta: 
        model = Book 

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


class BuscarLibroForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)
