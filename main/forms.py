from django import forms
from django.forms import ModelForm
from .models import ExInSolver, Solver, Categories


class SearchForm(forms.Form, ModelForm):
    number_ex = forms.IntegerField(
        label='Номер задания',

    )
