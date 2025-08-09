from django import forms
from .models import Role
from django.core.exceptions import ValidationError
from django.utils import timezone
from ckeditor.widgets import CKEditorWidget
class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter role name'
            })
        }
        labels = {
            'name': 'Role Name'
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError("Role name cannot be empty!")
        return name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
