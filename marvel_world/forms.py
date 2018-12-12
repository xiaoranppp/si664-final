from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from marvel_world.models import Character,Power


class CharacterForm(forms.ModelForm):
	class Meta:
		model = Character
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'submit'))
class PowerForm(forms.ModelForm):
	class Meta:
		model = Power
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'submit'))