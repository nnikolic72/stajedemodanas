from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from deliverers.models import Deliverer


class DelivererForm(forms.ModelForm):
    class Meta:
        model = Deliverer
        fields = ('name', 'phone',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save deliverer'))
