from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'published_date', 'image']
        labels = {
            'title': 'Nombre de la camiseta',
            'author': 'Equipo',
            'description': 'Descripción',
            'published_date': 'Año de temporada',
            'image': 'Imagen',
        }
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
