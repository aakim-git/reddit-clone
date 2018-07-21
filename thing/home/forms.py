from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):
    post = forms.CharField()

    class Meta:
        model = Post  # this is the model the modelForm is associated with
        fields = ('post',) # the comma is necessary to make it a tuple


