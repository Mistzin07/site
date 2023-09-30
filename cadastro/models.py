from django.db import models

class Aluno(models.Model):
    foto =models.ImageField(upload_to='fotos') 
    nome =models.CharField(max_length=250)
    idade =models.IntegerField()
    endereco =models.CharField(max_length=250)
    cpf = models.CharField(max_length=11)
    cep =models.CharField(max_length=8) 
    email =models.EmailField()
    contato =models.CharField(max_length=9)
        
    def __str__(self):
        return self.nome
