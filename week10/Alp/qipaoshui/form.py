# Author Andy Fang
# -*- coding:utf-8 -*-

from django import forms
from time import  timezone
class SearchForm(forms.Form):
    date = forms.DateField(label='舆情收集日期', widget=forms.DateInput(attrs={'type':'date'}))