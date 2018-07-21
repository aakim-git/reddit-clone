from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):
    post = forms.CharField(widget = forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Write a Post!'
        }
    )) # this is how to add html to forms
    
    class Meta:
        model = Post  # this is the model the modelForm is associated with
        fields = ('post',) # the comma is necessary to make it a tuple


