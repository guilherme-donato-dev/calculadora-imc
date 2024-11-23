from django import forms
from imc.models import calculadoraIMC

class calculadoraIMCModelForm(forms.ModelForm):

    class Meta:
        model = calculadoraIMC
        fields = '__all__'