from django.db import models

class Subtarefa(models.Model):
     # Tarefa.id_tarefa = models.AutoField(foreign_key=True, serialize=False, verbose_name='ID_tarefa')
     id_subtarefa = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
     nome_subtarefa = models.CharField(max_length=45, blank=False)
     anexo_subtarefa = models.FileField()
     status_subtarefa = models.CharField(max_length=7, blank=False, default='a fazer')

     def __str__(self):  # retorna o nome na lista (admin - DB)
         return self.nome_subtarefa