from django import forms 
from .models import Goal, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'description', 'amountsaved', 'email')

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ('description', 'cost', 'amountsaved', 'user', 'title')

