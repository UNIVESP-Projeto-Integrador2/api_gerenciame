from django.db import models


class Tarefa(models.Model):
    id_tarefa = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nome_tarefa = models.CharField(max_length=50, blank=False)
    data_inicial = models.DateField(blank=False)
    data_limite = models.DateField(blank=False)
    hora = models.TimeField(blank=False)
    status = models.IntegerField(blank=False, default=0, max_length=100)
    descricao = models.CharField(max_length=250)
#    subtarefas = models.ForeignObject(one_to_many=True)

    def __str__(self):  # retorna o nome na lista (admin - DB)
        return self.nome_tarefa


# class Subtarefa(models.Model):
#     id_tarefa = models.AutoField(foreign_key=True, serialize=False, verbose_name='ID')
#     id_subtarefa = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
#     nome_subtarefa = models.CharField(max_length=45, blank=False)
#     anexo_subtarefa = models.FileField()
#     status_subtarefa = models.CharField(max_length=7, blank=False, default='a fazer')
#
#     def __str__(self):  # retorna o nome na lista (admin - DB)
#         return self.nome_subtarefa
