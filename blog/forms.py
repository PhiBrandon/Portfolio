from django import forms

class contactForm(forms.Form):
	name = forms.CharField(label='Your name')
	email = forms.EmailField(label="Your Email")
	text = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 10}), label="message", required=False)