# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:02:50 2019

@author: Utilisateur
"""
from django import forms
from .models import Prototype, Level



class PrototypeForm(forms.ModelForm):
    
    class Meta:
        model = Prototype
        fields = '__all__'

class LevelForm(forms.ModelForm):

	class Meta:
		model = Level
		fields = '__all__'

