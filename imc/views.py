from django.shortcuts import render
from imc.forms import calculadoraIMCModelForm

# Create your views here.
def imc_view(request):
    if request.method == 'POST':
        imc_form = calculadoraIMCModelForm(request.POST)
        return render(request, 'imc.html', {'imc_form' : imc_form}  )
