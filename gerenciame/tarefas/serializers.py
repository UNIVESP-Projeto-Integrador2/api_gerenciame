from rest_framework import serializers
from .models import Tarefa


class TarefaSerializer(serializers.ModelSerializer):  # serializer: translates our data to and from JSON
    class Meta:
        model = Tarefa
        fields = ('id_tarefa', 'nome_tarefa', 'data_inicial', 'data_limite', 'hora', 'status', 'descricao')
        # falta subtarefas
        # itens que surgem obrigatoriamente + o q esta na Model


# class SubtarefaSerializer(serializers.ModelSerializer):  # serializer: translates our data to and from JSON
#     class Meta:
#         model = Subtarefa
#         fields = ('nome_subtarefa', 'anexo_subtarefa', 'status_subtarefa')
#         # itens que surgem obrigatoriamente + o q esta na Model
