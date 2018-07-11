#these are custom forms if we don't want the default login, etc. forms
from django import forms
from django.contrib.auth.models import User #this is the default hashed username, password info, etc. 
from django.contrib.auth.forms import UserCreationForm

#this is python inheritance. We are just extending the default User Form
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = False)

    class Meta: 
        model = User
        fields = {'username',
                  'first_name', 
                  'last_name', 
                  'email', 
                  'password1',
                  'password2'
                  } #password1 & 2 are for the verifying password thing. 

    def save(self, commit = True):
        user = super(RegistrationForm, self).save(commit = False) #if the user is not finished completing the form, you save the data. 
        user.first_name = self.cleaned_data['first_name'] #no weird inputs
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit == True:
            user.save() #the info is stored into the database. 
            
        return user


