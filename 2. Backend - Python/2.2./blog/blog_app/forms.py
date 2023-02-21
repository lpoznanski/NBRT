from django import forms

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
class EditPostForm(forms.Form):
    pass