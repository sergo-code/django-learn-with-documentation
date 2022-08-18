from django import forms
from .models import Publication


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title']
        # fields = '__all__'
        # exclude = ['title']


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    age = forms.IntegerField(max_value=10)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)