from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible

from .models import PrepodCategory, Prepod


input_widgets = {'class': 'form-control'}
select_widgets = {'class': 'form-select'}

class AddPrepodPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=PrepodCategory.objects.all(), empty_label='Категория не выбрана', label='Категории')

    class Meta:
        model = Prepod
        fields = ['name', 'slug', 'age', 'nickname', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5, 'class': 'form-control'}),
            'name': forms.TextInput(attrs=input_widgets),
            'slug': forms.TextInput(attrs=input_widgets),
            'age': forms.TextInput(attrs=input_widgets),
            'nickname': forms.TextInput(attrs=input_widgets),
            'photo': forms.FileInput(attrs=input_widgets),
            'is_published': forms.Select(attrs=select_widgets),
            'cat': forms.Select(attrs=select_widgets),

        }
        labels = {'slug': 'URL'}


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))


class EditPrepodPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=PrepodCategory.objects.all(), empty_label='Категория не выбрана', label='Категории')

    class Meta:
        model = Prepod
        fields = ['name', 'age', 'nickname', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5, 'class': 'form-control'}),
            'name': forms.TextInput(attrs=input_widgets),
            'slug': forms.TextInput(attrs=input_widgets),
            'age': forms.TextInput(attrs=input_widgets),
            'nickname': forms.TextInput(attrs=input_widgets),
            'photo': forms.FileInput(attrs=input_widgets),
            'is_published': forms.Select(attrs=select_widgets),
            'cat': forms.Select(attrs=select_widgets),

        }