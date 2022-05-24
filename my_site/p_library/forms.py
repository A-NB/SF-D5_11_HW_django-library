from dataclasses import field
from socket import fromshare
from django import forms
from django.utils.translation import gettext as _
from p_library.models import Author, Book, PublishingHouse


class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):
    ISBN = forms.CharField(
        max_length=13,
        label=_("Международный стандартный "
                    "книжный номер"),
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
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", })        
    )
    copy_count = forms.IntegerField(
        label=_("Количество копий"),        
        required=False,
        # default=1,
        widget=forms.TextInput(attrs={"class": "form-control", })          
    )
    price = forms.DecimalField(
        max_digits=12,
        decimal_places=2,
        label=_("Цена"),
        widget=forms.TextInput(attrs={"class": "form-control", })          
    )
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        # max_length=150,            
        label=_("Автор"),

        required=False, 

        # widget=forms.TextInput(attrs={"class": "form-control", })  
        # 
        widget=forms.Select(attrs={"class": "form-control", })          
    )        
    publishing_house = forms.ModelChoiceField(
        queryset=PublishingHouse.objects.all(),        
        # max_length=150,            
        label=_("Издательство"),
        required=False,        
        widget=forms.Select(attrs={"class": "form-control", }) 
    )
    year_publishing = forms.IntegerField(
        label=_("Год издания"),
        required=False,  
        widget=forms.TextInput(attrs={"class": "form-control", })         
    )
    # friends = forms.ComboField( #MultipleChoiceField
    #     label=_("Сейчаc читают"),
    #     required=False, 
    #     fields=(),
    #     widget=forms.Select(attrs={"class": "form-control", })  
    # )

    class Meta:
        model = Book
        fields = '__all__'


class PublisherForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = PublishingHouse
        fields = '__all__'    