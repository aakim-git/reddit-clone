from django import forms
from home.models import Post, Comment

class create_post_form(forms.ModelForm):
    title = forms.CharField(max_length = 100)
    post = forms.CharField(max_length = 5000, widget = forms.Textarea())
    link = forms.CharField(max_length = 100, required = False)
   
    class Meta:
        model = Post  
        fields = {
            'title',
            'post',
            'link',
        } 


class submit_comment_form(forms.ModelForm):
    text = forms.CharField(max_length = 5000)
   
    class Meta:
        model = Comment  
        fields = {
			'text'
		} 



