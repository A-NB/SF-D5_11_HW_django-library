# from dataclasses import field
# from email.policy import default
# from socket import fromshare
from django import forms
from django.utils.translation import gettext as _
from p_library.models import Author, Book, Publisher, Reader
from django.core.exceptions import ValidationError


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'    

    full_name = forms.CharField(
        max_length=150,            
        label=_("Полное имя автора"),        
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    birth_year = forms.IntegerField(
        label=_("Год рождения"),
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", })        
    ) 
    country = forms.CharField(
        max_length=2,            
        label=_("Страна"),        
        widget=forms.TextInput(attrs={"class": "form-control"})
    )       


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    ISBN = forms.CharField(
        max_length=13,
        label="ISBN",
        widget=forms.TextInput(attrs={"class": "form-control", })
    )
    title = forms.CharField(
        max_length=150,            
        label=_("Название"),
        widget=forms.TextInput(attrs={"class": "form-control", })            
    )
    description = forms.CharField(
        label=_("Аннотация"),
        required=False,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 5, })              
    )
    year_release = forms.IntegerField(
        label=_("Год выхода в свет"),
        widget=forms.TextInput(attrs={"class": "form-control", })        
    )
    copy_count = forms.IntegerField(
        label=_("Количество копий"),        
        required=False,
        min_value=1,
        initial=1,        
        widget=forms.NumberInput(attrs={"class": "form-control", })
    )
    price = forms.DecimalField(
        max_digits=12,
        decimal_places=2,
        label=_("Цена"),
        widget=forms.TextInput(attrs={"class": "form-control", })          
    )
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        label=_("Автор"),
        empty_label=_("Неизвестен"),
        initial=_("Неизвестен"),        
        required=False, 
        widget=forms.Select(attrs={"class": "form-control", })    
    )        
    publisher = forms.ModelChoiceField(
        queryset=Publisher.objects.all(),        
        label=_("Издательство"),
        empty_label=_("Неизвестно"), 
        initial=_("Неизвестно"),
        required=False,        
        widget=forms.Select(attrs={"class": "form-control", }) 
    )
    year_publishing = forms.IntegerField(
        label=_("Год издания"),
        widget=forms.TextInput(attrs={"class": "form-control", })         
    )
    readers = forms.ModelMultipleChoiceField(
        queryset=Reader.objects.all(),     
        label=_("Сейчаc читают"),
        required=False, 
        widget=forms.CheckboxSelectMultiple()
    )

    def clean_readers(self):
        readers = self.cleaned_data['readers']
        copy_count = self.cleaned_data['copy_count']
        if len(readers) > copy_count:
            raise forms.ValidationError(f'Количество копий ограничено ({copy_count})')
        return readers


class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = '__all__'   

    name = forms.CharField(
        max_length=150,            
        label=_("Полное имя читателя"),        
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    address = forms.CharField(
        max_length=150,            
        label=_("Адрес"),        
        widget=forms.TextInput(attrs={"class": "form-control"})
    )       


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'  
            
    name = forms.CharField(
        max_length=150,            
        label=_("Название издательства"),        
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    country = forms.CharField(
        max_length=2,            
        label=_("Страна"),        
        widget=forms.TextInput(attrs={"class": "form-control"})
    )       
    city = forms.CharField(
        max_length=150,            
        label=_("Город"),        
        widget=forms.TextInput(attrs={"class": "form-control"})       
    )
  