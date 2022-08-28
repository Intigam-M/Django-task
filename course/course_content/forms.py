from dataclasses import field
from tkinter import Widget
from xml.dom import ValidationErr
from django import forms
from .models import Tag, Lesson, Course
from django.core.exceptions import ValidationError



class TagForm(forms.ModelForm):
    class Meta:
        model =Tag
        fields = '__all__'


    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if title:
            if Tag.objects.filter(title__iexact = title).exists():
                raise ValidationError('Bu tag artiq movcudur!', code ='100')





class CourseForm(forms.ModelForm):
    class Meta:
        model =Course
        fields = '__all__'
        widgets = {
            'rank':forms.NumberInput(attrs={'max':5, 'min':1}),
            'description':forms.Textarea(attrs={'placeholder':'aciqlama girin'})
        }



class LessonForm(forms.ModelForm):
    class Meta:
        model =Lesson
        exclude=['view_count']


class CourseSearchForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control search-input', 'placeholder': 'Search'})) 


class CoursePriceForm(forms.Form):
    min_value = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control search-input', 'placeholder': 'Min Value'}))
    max_value = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control search-input', 'placeholder': 'Max Value'}))


    def clean(self):
        cleaned_data = super().clean()
        if 'min_value' in cleaned_data and 'max_value' in cleaned_data:
            if cleaned_data.get('max_value') < cleaned_data.get('min_value'):
                raise ValidationError('Max minden kicik ola bilmez!')