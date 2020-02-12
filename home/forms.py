from django import forms

class PostForm(forms.Form):
    photo       = forms.ImageField()
    user_id     = forms.IntegerField()
    pub_date    = forms.DateTimeField() 
    post_text   = forms.CharField(max_length=200)