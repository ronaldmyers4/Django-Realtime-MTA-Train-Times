from django import forms
from TrainTimes import views	

class TrainChoice(forms.Form):
	train_choice = forms.CharField(label='Train Choice',max_length=100)
	stop_choice = forms.CharField(label='Stop Choice', max_length=100)
	#UpDown = forms.CharField(label='Uptown or Downtown',max_length=100)

