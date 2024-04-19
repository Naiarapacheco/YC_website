from django import forms 

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('categoria', 'nome', 'descricao', 'price', 'image',)
        widgets = {
            'categoria': forms.Select(attrs={
                'class': INPUT_CLASSES
                }),
            'nome': forms.TextInput(attrs={
                'class': INPUT_CLASSES
                }),
            'descricao': forms.TextInput(attrs={
                'class': INPUT_CLASSES
                }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
                }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
                }),
            }