from django.db import models

# Create your models here.

class calculadoraIMC(models.Model):
    nome = models.CharField(max_length= 50, blank=True, null=True)
    altura = models.FloatField(max_length=10,blank=True, null=True)
    peso = models.FloatField(max_length=10, blank=True, null=True)
    imc = models.FloatField(blank=True, null=True)

    def resultado(self):
        if self.altura and self.peso:
            self.imc = self.peso / (self.altura ** 2)
            return self.imc
        
    '''def save(self, *args, **kwargs):
        self.calcular_imc() #calcula o imc antes de salvar
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} - IMC:{self.imc:.2f}"'''