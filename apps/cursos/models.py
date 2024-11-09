from django.db import models

# Create your models here.
class Cursos(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    carga_horaria = models.IntegerField()
    # instrutor = (será implementado assim que model de professores estiver pronto)
    
    def __str__(self):
        return self.titulo 