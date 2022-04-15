from django import forms
from .models import Ai1


class AiForm(forms.ModelForm):
    class Meta:
        model = Ai1
        fields = '__all__'
        widgets = {'user': forms.HiddenInput}


AiForms = forms.modelformset_factory(Ai1, fields='__all__', can_delete=True,
                                     widgets={'user': forms.HiddenInput}, extra=0)
