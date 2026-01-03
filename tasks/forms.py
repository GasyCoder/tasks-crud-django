from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "is_done"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Titre"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Description (optionnel)"}),
        }
