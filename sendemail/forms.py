from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(required=True,widget= forms.TextInput(
    	attrs={'placeholder':'Your name','class':'form-control'}))
    from_email = forms.EmailField(required=True,widget= forms.TextInput(
    	attrs={'placeholder':'Your email','class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(
    	attrs={'placeholder':'Your message','class':'form-control'}), required=True)
