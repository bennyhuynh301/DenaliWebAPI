from django import forms


class UploadParentsLogFileForm(forms.Form):
    file_name = forms.CharField(max_length=100)
    parent_log = forms.FileField()

