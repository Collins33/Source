from django import forms#import forms module
from .models import Article

class NewsLetterForm(forms.Form):
    your_name=forms.CharField(label="first_name",max_length=30)
    email=forms.EmailField(label="Email")
    


class NewsArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        exclude=['editor','pub_date']
        widget={
        'tags':forms.CheckboxSelectMultiple(),
        }
