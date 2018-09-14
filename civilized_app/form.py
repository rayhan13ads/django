from django import forms
from .models import FileUploadModel
class UploadFileForm(forms.ModelForm):
    
    class Meta:
        model = FileUploadModel
        fields = ['name', 'file_name']
        widgets = {
        'name':forms.TextInput(attrs = {'class': 'form-control','placeholder':'Enter your Name', 'id':'name'}),
        'file_name':forms.FileInput( attrs = {'class': 'form-control-file', 'id':'filepath'})
        }

