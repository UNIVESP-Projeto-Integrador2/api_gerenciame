from django.db import models
from .subtarefa_model import Subtarefa

class Tarefa(models.Model):
    id_tarefa = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nome_tarefa = models.CharField(max_length=50, blank=False)
    data_inicial = models.DateField(blank=False)
    data_limite = models.DateField(blank=False)
    hora = models.TimeField(blank=False)
    status = models.IntegerField(blank=False, default=0, max_length=100)
    descricao = models.CharField(max_length=250)
    subtarefas = [Subtarefa]
    def __str__(self):  # retorna o nome na lista (admin - DB)
        return self.nome_tarefa






