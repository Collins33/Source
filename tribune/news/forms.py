from django import forms#import forms module

class NewsLetterForm(forms.Form):
    your_name=forms.CharField(label="first_name",max_length=30)
    email=forms.EmailField(label="Email")
