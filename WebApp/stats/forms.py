from django import forms

class RoomRequestForm(forms.Form):
	room = forms.CharField(label='roomID', max_length='5')
