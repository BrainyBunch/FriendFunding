from django import forms 
from .models import Goal, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'photo_url', 'nationality')

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ('user', 'title', 'album')