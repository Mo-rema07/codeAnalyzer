from django import forms


class CodeSnippetForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea)


class UploadFileForm(forms.Form):
    file = forms.FileField()
