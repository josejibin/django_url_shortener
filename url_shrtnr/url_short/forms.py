from django import forms 

class UrlForm(forms.Form):
	original_url = forms.CharField()
	
	#text = forms.CharField(widget=forms.Textarea())
