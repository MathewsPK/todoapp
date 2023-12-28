from.models import Todo
from django import forms
class todoforms(forms.ModelForm):
    class Meta:
        model = Todo
        fields=['title','description','due_date',]

