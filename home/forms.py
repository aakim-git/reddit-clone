from django import forms
from home.models import Post, Comment

class create_post_form(forms.ModelForm):
    title = forms.CharField(max_length = 100)
    post_content = forms.CharField(max_length = 5000, widget = forms.Textarea())
    link = forms.CharField(max_length = 100, required = False)
   
    class Meta:
        model = Post  
        fields = {
            'title',
            'post_content',
            'link',
        } 


class submit_comment_form(forms.ModelForm):
    text = forms.CharField(max_length = 5000)
   
    class Meta:
        model = Comment  
        fields = {
			'text'
		} 

    def __init__(self, *args, **kwargs):
        super(submit_comment_form, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class' : 'submit_comment_form'})


