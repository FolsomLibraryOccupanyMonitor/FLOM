from django import forms

class RoomRequestForm(forms.Form):
	room = forms.CharField(label='Room ID', max_length='5')
