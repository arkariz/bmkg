from django import forms
from django.forms import widgets
from .models import BukuTamu

class FormBukuTamu(forms.ModelForm):
    class Meta:
        model = BukuTamu
        fields = ('nama', 'alamat', 'telepon', 'email', 'instansi', 'tanggal', 'keperluan')

        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'telepon': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
            'instansi': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'tanggal': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'keperluan': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
        }